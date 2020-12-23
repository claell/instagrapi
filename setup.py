from setuptools import setup, find_packages

long_description = '''
Fast and effective Instagram Private API wrapper (public+private requests and challenge resolver).

Use the most recent version of the API from Instagram.

### Features

1. Performs Public API (web, anonymous) or Private API (mobile app, authorized) requests depending on the situation (to avoid Instagram limits)
2. Challenge Resolver have Email (as well as recipes for automating receive a code from email) and SMS handlers
3. Support upload a Photo, Video, IGTV, Albums and Stories
4. Support work with User, Media, Insights, Collections, Location (Place), Hashtag and Direct objects
5. Like, Follow, Edit account (Bio) and much more else
6. Insights by account, posts and stories
7. Build stories with custom background, font animation, swipe up link and mention users
8. In the next release, account registration and captcha passing will appear
'''

setup(
    name='instagrapi',
    version='1.3.2',
    author='Mikhail Andreev',
    author_email='x11org@gmail.com',
    license='MIT',
    url='https://github.com/adw0rd/instagrapi',
    install_requires=[
        'pytz==2020.1',
        'requests==2.24.0',
        'PySocks==1.7.1',
        'moviepy==1.0.3',
        'Pillow==7.2.0',
        'pydantic==1.7.2'
    ],
    keywords='instagram private api',
    description='Fast and effective Instagram Private API wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
