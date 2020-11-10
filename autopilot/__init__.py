from distutils.core import setup

setup(
    name="Distutils",
    version="1.0",
    description="""Self driving car module
     for any game and also real life projects""",
    author="Tomasz Derek",
    author_email="tomasz_derek@wp.pl",
    url="hyperscypion.com",
    packages=open("../requirements", "w").readlines(),
)
