from setuptools import setup, find_packages

setup(
    name="gohApibeta",
    version="0.1.1",  # обновите версию
    author="GohHacked",
    description="GPT client library",
    packages=find_packages(),
    install_requires=[
        "requests",  # и другие зависимости
    ],
    python_requires='>=3.7',
)