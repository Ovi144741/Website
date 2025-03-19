import streamlit as st
import datetime

# ---- PAGE CONFIG ----
st.set_page_config(page_title="My Modern Blog", layout="wide")

# ---- CUSTOM STYLING ----
st.markdown("""
    <style>
        /* Background Color */
        body {
            background-color: #f8f9fa;
        }

        /* Main Title */
        .main-title {
            text-align: center;
            font-size: 3rem;
            font-weight: bold;
            color: #333;
        }

        /* Blog Post Title */
        .post-title {
            font-size: 2rem;
            font-weight: bold;
            color: #007BFF;
        }

        /* Post Content */
        .post-content {
            font-size: 1.1rem;
            color: #444;
        }

        /* Date */
        .post-date {
            font-size: 0.9rem;
            color: #888;
        }

        /* Navigation Sidebar */
        .css-1d391kg {
            background-color: #343a40 !important;
            color: white !important;
        }

        /* Success Message */
        .stAlert {
            background-color: #d4edda !important;
            color: #155724 !important;
            border-left: 5px solid #28a745 !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---- SIDEBAR NAVIGATION ----
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio("Go to", ["🏠 Home", "📝 New Post", "👤 About"])

# Initialize session state for blog posts
if "posts" not in st.session_state:
    st.session_state.posts = []

# ---- HOME PAGE ----
if menu == "🏠 Home":
    st.markdown('<h1 class="main-title">📖 My Modern Blog</h1>', unsafe_allow_html=True)
    st.write("Welcome to my personal blog! Explore my latest posts below. 🚀")

    if not st.session_state.posts:
        st.info("No blog posts yet. Click on 'New Post' to add one!")
    else:
        for post in reversed(st.session_state.posts):
            with st.container():
                st.markdown(f'<h2 class="post-title">{post["title"]}</h2>', unsafe_allow_html=True)
                st.markdown(f'<p class="post-date">📝 {post["date"]}</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="post-content">{post["content"]}</p>', unsafe_allow_html=True)
                st.markdown("---")

# ---- NEW POST PAGE ----
elif menu == "📝 New Post":
    st.markdown('<h1 class="main-title">📝 Write a New Blog Post</h1>', unsafe_allow_html=True)

    with st.form("blog_form"):
        title = st.text_input("Post Title", placeholder="Enter a catchy title...")
        content = st.text_area("Post Content", placeholder="Write something amazing...", height=200)
        submitted = st.form_submit_button("🚀 Publish Post")

        if submitted and title and content:
            st.session_state.posts.append({
                "title": title,
                "content": content,
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success("🎉 Your blog post has been published!")

# ---- ABOUT PAGE ----
elif menu == "👤 About":
    st.markdown('<h1 class="main-title">👤 About Me</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("https://via.placeholder.com/200", width=200)

    with col2:
        st.write("Hi! I'm a passionate blogger who loves sharing insights and experiences. 🌎")
        st.write("This blog is built using [Streamlit](https://streamlit.io/). Hope you enjoy reading!")

