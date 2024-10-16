from setuptools import setup, find_packages

setup(
    name="opennife",
    version="0.1.0",
    description="A tool to extract frames using OpenNI, the tool extract 8bit and 16bit depth images",
    author="Lucas Amorim",
    author_email="amorimlucas416@gmail.com",
    url="https://github.com/lucasrbk/Opennife",
    packages=find_packages(),
    install_requires=[
        "openni==1.0.0",
        "opencv-python==4.5.3",
        "numpy==1.21.0"
    ],
    extras_require={
        "dev": [
            "pytest==6.2.4"
        ]
    },
    python_requires='>=3.8',
    project_urls={
        "Homepage": "https://github.com/lucasrbk/Opennife",
        "Issues": "https://github.com/lucasrbk/Opennife/issues"
    },
)

