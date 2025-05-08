import streamlit as st

# Clear inputs when restarting
if "restart" not in st.session_state:
    st.session_state.restart = False

if st.session_state.restart:
    st.session_state.clear()
    st.experimental_rerun()

st.title("🌩️ Choose Your Own Adventure")
st.write("The day started off great—clear skies and a warm breeze. A perfect day for a walk.")
st.write("As you were on your walk, the wind started to pick up and the skies turned grey...")

choice1 = st.text_input("Do you want to continue walking, or find somewhere to wait out the storm? (continue/wait)").strip().lower()

if choice1 == "wait":
    choice2 = st.text_input("You run over to a nearby shack. Do you want to go in, or wait under a nearby tree? (shack/tree)").strip().lower()

    if choice2 == "tree":
        st.success("🌳 Good idea! You waited out the storm and can now return home safe.")
        choice3 = st.text_input("You see something shiny in the grass. What do you do? (pick it up/ignore)").strip().lower()

        if choice3 == "pick it up":
            st.success("💎 It's a magical coin that brings you luck forever. You live a happy life. The end!")
            if st.button("Restart"):
                st.session_state.restart = True
                st.experimental_rerun()

        elif choice3 == "ignore":
            st.write("You leave it alone and walk home safely. Life goes on. The end.")
            if st.button("Restart"):
                st.session_state.restart = True
                st.experimental_rerun()

        elif choice3 != "":
            st.write("That wasn't an option. Your story ends here.")
            if st.button("Restart"):
                st.session_state.restart = True
                st.experimental_rerun()

    elif choice2 == "shack":
        st.write("🧙‍♀️ Bad choice! You opened the door and were trapped by a witch.")
        choice4 = st.text_input("The witch gives you a chance to escape. What do you do? (accept/refuse)").strip().lower()

        if choice4 == "accept":
            st.success("🧹 You completed the task and the witch lets you go. You return home safely. The end!")
            if st.button("Restart"):
                st.session_state.restart = True
                st.experimental_rerun()

        elif choice4 == "refuse":
            st.write("🐸 You tried to run and got turned into a frog. The end.")
            if st.button("Restart"):
                st.session_state.restart = True
                st.experimental_rerun()

        elif choice4 != "":
            st.write("That wasn't an option. Your story ends here.")
            if st.button("Restart"):
                st.session_state.restart = True
                st.experimental_rerun()

    elif choice2 != "":
        st.write("That wasn't an option. Your story ends here.")
        if st.button("Restart"):
            st.session_state.restart = True
            st.experimental_rerun()

elif choice1 == "continue":
    st.write("⚡ Bad choice. You got struck by lightning. The end.")
    if st.button("Restart"):
        st.session_state.restart = True
        st.experimental_rerun()

elif choice1 != "":
    st.write("That wasn't an option. Your story ends here.")
    if st.button("Restart"):
        st.session_state.restart = True
        st.experimental_rerun()
