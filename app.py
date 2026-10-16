import streamlit as st

if "profile" not in st.session_state:
    st.session_state.profile = {
        "name" : "",
        "gender" : ""
    }

st.title("Health Pal")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Profile",
        "Workout",
        "Nutrition",
        "Medication",
        "Menstrual Cycle",
        "Progress"
    ]
)

if page == "Home":
    st.header("How are you feeling today?")

    message = st.text_input("Tell me what's on your mind")

    if st.button("Share"):
        if message:
            st.write("Health Pal:", message)
        else:
            st.warning("Tell me something first.")

elif page == "Profile":
    st.header("Your Profile")

    if "profile_gender" not in st.session_state:
        st.session_state.profile_gender = (
            st.session_state.profile["gender"]
            or "Female"
        )

    name = st.text_input(
        "Name",
        value=st.session_state.profile["name"]
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male", "Prefer not to say"],
        key="profile_gender"
    )

    if st.button("Save Profile"):
        st.session_state.profile["name"] = name
        st.session_state.profile["gender"] = gender
        st.success("Profile saved!")

elif page == "Workout":
    st.header("Workout")

elif page == "Nutrition":
    st.header("Nutrition")

elif page == "Medication":
    st.header("Medication")

elif page == "Menstrual Cycle":
    st.header("Menstrula Cycle")

elif page == "Progress":
    st.header("Progress")