import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

authors = [
    {
        "Name" : "Aadam Lokhandwla",
        "Email" : "aadamlokhandwala786@gmail.com",
    },
    {
        "Name" : "Murtaza Cyclewala",
        "Email" : "murtazacyclewala27@gmail.com",
    },
    {
        "Name" : "Krutik Parmar" ,
        "Email" : "krutikparmar106@gmail.com", 
    },
    {
        "Name" : "Samarth Jain",
        "Email" : "samarth16022002@gmail.com",
    },    
]

authors_string = ""
for author in authors:
    authors_string += author["Name"] + " <" + author["Email"] + ">, "
authors_string = authors_string[:-2]

setuptools.setup(
    name="auto-whatsapp",
    version="0.0.1",
    author=authors_string,
    author_email="aadamlokhandwala786@gmail.com",
    description="Helps Automate whatsapp, all tools provided to make a bot out of it.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AadamLok/python_whatsapp_lib",
    project_urls={
        "Bug Tracker": "https://github.com/AadamLok/python_whatsapp_lib/issues",
    },
    keywords = ["Automate WhatsApp"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
