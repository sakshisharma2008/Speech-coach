import base64

import pandas as pd
import requests
import streamlit as st

st.set_page_config(page_title="Speech Coach", page_icon="🎤", layout="wide")
st.title("🎤 Speech Coach")

# Sidebar: Colab server URL and language
url = st.sidebar.text_input(
    "Colab Server URL",
    placeholder="https://xxxx.trycloudflare.com"
)

lang = st.sidebar.selectbox("Language", ["en", "hi"])

recording = st.audio_input("Record your speech (speak 3-4 sentences)")

if recording and st.button("Analyze"):
    if not url:
        st.error("Please enter the Colab URL in the sidebar.")
        st.stop()

    with st.spinner("Analyzing your speech on Colab... (20-40 seconds)"):
        try:
            # Send recording to Colab
            response = requests.post(
                url.rstrip("/") + "/analyze",
                files={
                    "file": (
                        "recording.wav",
                        recording.getvalue(),
                        "audio/wav"
                    )
                },
                data={"lang": lang},
                timeout=300,
            )

            response.raise_for_status()
            data = response.json()

        except Exception as e:
            st.error(f"Could not connect to Colab: {e}")
            st.stop()

    results = data["results"]

    if not results:
        st.warning("No sentences were detected. Please speak a little longer and more clearly.")
        st.stop()

    # ---------- Summary ----------
    problem_count = sum(1 for r in results if r["tips"])
    avg_wpm = sum(r["rate"] or 0 for r in results) / len(results) * 60

    c1, c2, c3 = st.columns(3)

    c1.metric("Sentences", len(results))
    c2.metric("Average Speed", f"{avg_wpm:.0f} words/min")
    c3.metric("Problematic Sentences", problem_count)

    # ---------- Transcript ----------
    with st.expander("Transcript"):
        st.write(data["transcript"])

    # ---------- Graph ----------
    st.subheader("Speech Feature Graph")

    st.image(
        base64.b64decode(data["graph"]),
        caption="Green = IDEAL range | Red = problematic sentences (S1, S2...)"
    )

    # ---------- Sentence-wise result ----------
    st.subheader("How to Improve Your Speech")

    for i, item in enumerate(results, start=1):

        if item["tips"]:
            st.error(f"❌ S{i}: {item['sentence']}")

            for tip in item["tips"]:
                st.write("→", tip)

        else:
            st.success(f"✅ S{i}: {item['sentence']}")

    # ---------- Numbers ----------
    st.subheader("Detailed Analysis")

    table = pd.DataFrame(results).drop(columns="tips")
    table.index = [f"S{i}" for i in range(1, len(table) + 1)]

    st.dataframe(table)

    # ---------- Audio ----------
    st.subheader("Listen and Compare")

    st.write("Your Recording:")
    st.audio(recording)

    st.write("Ideal Recording:")
    st.audio(
        base64.b64decode(data["ideal_audio"]),
        format="audio/mp3"
    )

    # ---------- Issues (with timestamps) ----------
    st.subheader("Detected Issues")

    if data["regions"]:
        st.dataframe(
            pd.DataFrame(data["regions"]).rename(
                columns={
                    "from": "From (s)",
                    "to": "To (s)",
                    "issue": "Issue"
                }
            )
        )
    else:
        st.success("No significant issues were detected 🎉")
