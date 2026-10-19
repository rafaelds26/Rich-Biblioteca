from setuptools import setup, find_packages

setup(
    name="rich-modelo",
    version="0.1.0",
    description="Biblioteca Python para a curva de Richards e janelas deslizantes",
    author="Rafael Santos",
    packages=find_packages(exclude=("testes", "testes.*", "exemplos", "exemplos.*")),
    install_requires=["numpy>=1.23", "scipy>=1.9"],
    python_requires=">=3.10",
)
