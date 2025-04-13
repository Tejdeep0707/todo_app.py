import streamlit as st

st.set_page_config(page_title="To-Do List", page_icon="✅", layout="centered")

# Background Styling
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://t3.ftcdn.net/jpg/05/13/59/72/360_F_513597277_YYqrogAmgRR9ohwTUnOM784zS9eYUcSk.jpg");
    background-size: cover;
    background-position: center;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
[data-testid="stSidebar"] {
    background-color: rgba(0,0,0,0.3);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("✅ To-Do List")

st.subheader("Add a new task")

# Task input
task_name = st.text_input("Enter task", key="task_input")

if st.button("➕ Add Task"):
    if task_name.strip():
        st.session_state.tasks.append({
            "name": task_name,
            "done": False
        })
        st.rerun()
    else:
        st.warning("Please enter a task.")

# Display all tasks
st.subheader("📋 Your Tasks")

if st.session_state.tasks:
    for idx, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([8, 2])
        with col1:
            st.markdown(
                f"**{'✅' if task['done'] else '🔲'} {task['name']}**",
                unsafe_allow_html=True
            )
        with col2:
            if st.button("✔️ Done", key=f"done_{idx}"):
                st.session_state.tasks[idx]["done"] = True
                st.rerun()
else:
    st.info("No tasks yet. Add something above!")

# Check completion status
st.markdown("---")
if st.button("🔍 Check if all tasks are completed"):
    if all(task["done"] for task in st.session_state.tasks):
        st.success("🎉 All tasks completed!")
    else:
        st.warning("🕒 Some tasks are still pending.")

# Clear All Button
if st.button("🧹 Clear All Tasks"):
    st.session_state.tasks.clear()
    st.success("All tasks cleared!")
    st.rerun()

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Tejdeep's To-Do App")
