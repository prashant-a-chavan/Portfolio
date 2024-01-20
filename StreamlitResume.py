import streamlit as st
from PIL import Image
import pandas as pd
# Set the page title
# st.write("## My Interactive Resume")

# Create a sidebar for navigation
st.sidebar.markdown("---")
selected_section = st.sidebar.radio("SECTIONS : ", ["Intro", "Education", "Skills", "Projects", "Achievements and Certifications"])
st.markdown(
    """
    <style>
    .css-ch5dnh {visibility: hidden;}
    .css-cio0dv {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)
# Header section
if selected_section == "Intro":
    st.header("About Me")
    # st.subheader("Currently pursuing MCA from JSS Science and Technology University Mysuru.")
    st.write("Hello there! I'm Prashant, hailing from Karnataka, India. Currently, I am pursuing a Master's in Computer Applications at JSS Science and Technology University in Mysuru. I successfully earned my Bachelor's degree from Karnataka Science College in Dharwad.")
    st.write("I am actively exploring opportunities for an entry-level position as a Software Engineer or an internship. My goal is to contribute my knowledge and skills to real-world projects. If you have any exciting opportunities, please feel free to connect!")

    st.write("Email: reposeful8887@gmail.com")
    st.write("Phone: +91 8197064954")
    st.write("LinkedIn: www.linkedin.com/in/c-prashant")
    st.write("GitHub: https://github.com/prashant-a-chavan")

# Education section
if selected_section == "Education":
    st.write("## Education")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    # Create a table for education details
    education_data = pd.DataFrame([
        ["JSS Science and Technology University Mysuru", "Pursuing MCA", "2023 - 2024", "8.57 CGPA"],
        ["Karnataka Science College Dharwad", "BCA", "2019 - 2022", "85.90 %"],
        ["Government PU College Kokatnur", "PUC", "2017 - 2019", "69.16 %"],
        ["Government High School Kokatnur", "SSLC", "2016 - 2017", "67.68 %"],
    ], columns=["Institution", "Degree", "Year", "Result"])

    # Display the DataFrame without index
    st.write(education_data.to_markdown(index=False))

# Skills section
if selected_section == "Skills":
    st.write("## Skills")
    st.write("""- ######  Programming Languages
              #include < JAVA, C++, C & PYTHON >""")
    st.write("""- ###### Web Development
            <HTML>
            HTML, CSS, Basic JAVASCRIPT, BOOTSTRAP
      </HTML>""")
    # st.markdown("---")
    # st.text("")
    st.write("- ###### Databases: SQL, MongoDB")
    st.write("- ###### Problem Solving, Data Structures and Algorithms, Team Collaboration")

# Projects section
if selected_section == "Projects":
    st.write("## Projects")

    # Project selection dropdown
    project_options = ["Select a Project","BasketXpert", "Student Attendance Management System"]
    selected_project = st.selectbox("",project_options)

    # Display selected project details
    if selected_project == "BasketXpert":
        st.subheader("Title : BasketXpert")
        st.write("Technology : Python")
        st.write("Tool : Visual studio code")
        st.write("Description : BasketXpert is a web application designed to revolutionize market basket analysis for businesses of small to medium sizes. Leveraging the power of Python and the mlextend library, provides an accessible and user-friendly platform for analyzing transactional data and gaining valuable insights into customer behavior and purchasing patterns.")
        st.write("Github : https://github.com/prashant-a-chavan/BasketXpert")
        st.markdown("---")
        st.subheader("Screenshots")
        st.text("")
        st.text("")
        st.image("Project Screenshot.JPG", use_column_width=True)

    elif selected_project == "Student Attendance Management System":
        st.subheader("Title : Student Attendance Management System")
        st.write("Technology : Python")
        st.write("Tool : Visual studio code")
        st.write("Description : A Python-based platform designed to streamline attendance tracking and management. Our system offers a user-friendly interface for students to access their attendance records and eligibility status, while empowering lecturers with features to effortlessly manage student records, track daily attendance, and access detailed attendance statistics.")
        st.write("Github : https://github.com/prashant-a-chavan/Student-Attendance-Management-System")
        st.markdown("---")
        st.subheader("Screenshots")
        st.text("")
        st.text("")
        st.image("Project Screenshot2.JPG", use_column_width=True)
    # elif selected_project == "Project 3":
    #     st.subheader("Project 3")
    #     st.write("Description of Project 3 goes here.")

# References section
if selected_section == "Achievements and Certifications":
    st.write("#### Achievements")

    achievements = pd.DataFrame([
    ["First Place, BITS AND BYTES(CODING) event in 'TAKSHAK 2K22 State Level IT Fest' Organized by: Karnataka University Dharwad"],
    ["Participation in 'EVOGEN 11.O' event  Organized by: KLS Gogte Institute of Technology Belagavi"]],columns=["Achievements"])
    st.write(achievements.to_markdown(index=False))
    st.markdown("")
    st.markdown("")
    st.markdown("")

    st.write("#### Certifications")

    achievements = pd.DataFrame([
    ["SQL (Basic) Certificate from HackerRank"],
    ["JAVA (Basic) Certificate from HackerRank"],
    ["WEB TECHNOLOGY 10 DAYS WORKSHOP from APPONIX academy"]],columns=["Achievements"])
    st.write(achievements.to_markdown(index=False))

st.sidebar.markdown(
    """
    <div style="position: relative; top: 15vh; text-align: left; width: 100%;">
        <p style="font-size: 12px;">gmail : reposeful8887@gmail.com</p>
        <p style="font-size: 12px;"><a href="https://drive.google.com/file/d/1ghUx8qwa_QzOg7Ifx_6Djytg6Xugjput/view?usp=drive_link" target="_blank">Click here for Resume</a></p>
    </div>
    """,
    unsafe_allow_html=True,
)
