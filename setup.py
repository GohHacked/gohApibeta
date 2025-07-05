from setuptools import setup, find_packages

setup(
    name="gohApibeta",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["g4f"],
    author="GohHacked",
    description="Обёртка для gpt с удобным интерфейсом",
    python_requires=">=3.7",
)