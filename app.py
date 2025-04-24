# app.py
"""
import streamlit as st
from src.qa_chain import get_qa_chain

# Page setup
st.set_page_config(page_title="Insurance Assistant", page_icon="🛡️", layout="centered")
st.markdown("<h1 style='text-align: center;'>🛡️ Insurance Policy Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Choose a topic or ask your own question.</p>", unsafe_allow_html=True)

qa_chain = get_qa_chain()

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "step" not in st.session_state:
    st.session_state.step = "intro"

if "feedback_given" not in st.session_state:
    st.session_state.feedback_given = False

# Step: Intro with Quick Topics
# Step: Intro with Quick Topics
if st.session_state.step == "intro":
    st.subheader("🧠 Frequently Asked Topics")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🏥 Health Insurance"):
            st.session_state.step = "chat"
            st.session_state.chat_history.append({"role": "user", "text": "Tell me about health insurance."})
            response = qa_chain("Tell me about health insurance.")
            st.session_state.chat_history.append({"role": "bot", "text": response})

    with col2:
        if st.button("🚗 Auto Insurance"):
            st.session_state.step = "chat"
            st.session_state.chat_history.append({"role": "user", "text": "Tell me about auto insurance."})
            response = qa_chain("Tell me about auto insurance.")
            st.session_state.chat_history.append({"role": "bot", "text": response})

    with col3:
        if st.button("💼 Life Insurance"):
            st.session_state.step = "chat"
            st.session_state.chat_history.append({"role": "user", "text": "Tell me about life insurance."})
            response = qa_chain("Tell me about life insurance.")
            st.session_state.chat_history.append({"role": "bot", "text": response})

    with col4:
        if st.button("🏠 Home Insurance"):
            st.session_state.step = "chat"
            st.session_state.chat_history.append({"role": "user", "text": "Tell me about home insurance."})
            response = qa_chain("Tell me about home insurance.")
            st.session_state.chat_history.append({"role": "bot", "text": response})

# Step: Chat Interface
if st.session_state.step == "chat":
    st.markdown("### 💬 Conversation")

    # Display history
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"🧑‍💼 **You**: {msg['text']}")
        else:
            st.markdown(f"🤖 **Bot**: {msg['text']}")

    # Input box
    user_input = st.text_input("Ask anything more about insurance:")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "text": user_input})
        with st.spinner("Thinking..."):
            bot_reply = qa_chain(user_input)
        st.session_state.chat_history.append({"role": "bot", "text": bot_reply})

    st.markdown("---")
    st.markdown("❓ Do you need more help?")
    col_yes, col_no = st.columns(2)
    with col_yes:
        if st.button("Yes, ask more"):
            pass  # Stay on chat screen
    with col_no:
        if st.button("No, I'm done"):
            st.session_state.step = "feedback"

# Step: Feedback Form
if st.session_state.step == "feedback" and not st.session_state.feedback_given:
    st.markdown("### ⭐ Rate your experience")
    rating = st.slider("How helpful was this chatbot?", 1, 5, 4)
    comment = st.text_area("Optional comment:")

    if st.button("Submit Feedback"):
        # Save or print feedback here
        st.session_state.feedback_given = True
        st.success("🎉 Thanks for your feedback!")
        st.balloons()

# Sidebar: Clear Chat
st.sidebar.title("⚙️ Options")
if st.sidebar.button("Reset Chat"):
    for key in ["chat_history", "step", "feedback_given"]:
        st.session_state.pop(key, None)
    st.experimental_rerun()

"""
import streamlit as st
from src.qa_chain import get_qa_chain

# Page setup
st.set_page_config(page_title="Insurance Assistant", page_icon="🛡️", layout="centered")
st.markdown("<h1 style='text-align: center;'>🛡️ Insurance Policy Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Choose a topic or ask your own question.</p>", unsafe_allow_html=True)

qa_chain = get_qa_chain()

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "step" not in st.session_state:
    st.session_state.step = "intro"

if "feedback_given" not in st.session_state:
    st.session_state.feedback_given = False

if "phone_number" not in st.session_state:
    st.session_state.phone_number = None

# Step: Intro with Quick Topics
if st.session_state.step == "intro":
    st.subheader("🧠 Frequently Asked Topics")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🏥 Health Insurance"):
            st.session_state.step = "chat"
            st.session_state.chat_history.append({"role": "user", "text": "Tell me about health insurance."})
            response = qa_chain("Tell me about health insurance.")
            st.session_state.chat_history.append({"role": "bot", "text": response})

    with col2:
        if st.button("🚗 Auto Insurance"):
            st.session_state.step = "chat"
            st.session_state.chat_history.append({"role": "user", "text": "Tell me about auto insurance."})
            response = qa_chain("Tell me about auto insurance.")
            st.session_state.chat_history.append({"role": "bot", "text": response})

    with col3:
        if st.button("💼 Life Insurance"):
            st.session_state.step = "chat"
            st.session_state.chat_history.append({"role": "user", "text": "Tell me about life insurance."})
            response = qa_chain("Tell me about life insurance.")
            st.session_state.chat_history.append({"role": "bot", "text": response})

    with col4:
        if st.button("🏠 Home Insurance"):
            st.session_state.step = "chat"
            st.session_state.chat_history.append({"role": "user", "text": "Tell me about home insurance."})
            response = qa_chain("Tell me about home insurance.")
            st.session_state.chat_history.append({"role": "bot", "text": response})

# Step: Chat Interface
if st.session_state.step == "chat":
    st.markdown("### 💬 Conversation")

    # Display history
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"🧑‍💼 **You**: {msg['text']}")
        else:
            st.markdown(f"🤖 **Bot**: {msg['text']}")

    # Input box
    user_input = st.text_input("Ask anything more about insurance:")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "text": user_input})
        with st.spinner("Thinking..."):
            bot_reply = qa_chain(user_input)
        st.session_state.chat_history.append({"role": "bot", "text": bot_reply})

    st.markdown("---")
    st.markdown("❓ Do you need more help?")

    col_yes, col_no = st.columns(2)
    
    with col_yes:
        if st.button("Yes, ask more"):
            pass  # Stay on chat screen
    
    with col_no:
        if st.button("No, I'm done"):
            st.session_state.step = "feedback"

    # Contact Human Agent
    if st.button("Contact Human Agent"):
        phone_number = st.text_input("Please enter your phone number:")
        
        if phone_number:
            st.session_state.phone_number = phone_number
            st.session_state.step = "feedback"
            st.success("Thank you! A human agent will contact you soon.")
        else:
            st.warning("Please enter a valid phone number.")

# Step: Feedback Form
if st.session_state.step == "feedback" and not st.session_state.feedback_given:
    st.markdown("### ⭐ Rate your experience")
    rating = st.slider("How helpful was this chatbot?", 1, 5, 4)
    comment = st.text_area("Optional comment:")

    if st.button("Submit Feedback"):
        # Save or print feedback here
        st.session_state.feedback_given = True
        st.success("🎉 Thanks for your feedback! Our team will reach out if needed.")
        st.balloons()

# Sidebar: Clear Chat
st.sidebar.title("⚙️ Options")
if st.sidebar.button("Reset Chat"):
    for key in ["chat_history", "step", "feedback_given", "phone_number"]:
        st.session_state.pop(key, None)
    st.experimental_rerun()
