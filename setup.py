from distutils.core import setup

setup(
	name         = 'jak',
	version      = "0.7",
	packages     = ['j'],
	url          = "https://vmnlopes.github.io/Jade-Application-Kit",
	license      = 'GPL',
	author       = "Vitor Lopes",
	author_email = "vmnlop@gmail.com",
	description  = 'Jade Application Kit, build awesome hybrid Web and Desktop applications.',
    download_url = "https://github.com/vmnlopes/Jade-Application-Kit/zipball/master",
    keywords     = ["gui", "webkit2", "html5", "web", "javascript", "python", "webgl", "css3", "pygobject", "gtk", "desktop", "gnome", "linux"],
    classifiers  = [
	    "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
        "Environment :: X11 Applications",
        "Environment :: X11 Applications :: Gnome",
        "Environment :: X11 Applications :: GTK",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        ],
    include_package_data=True,
    package_data={"j":["window.css"]},
    data_files=[
    ("/usr/bin/", ["bin/jak"]),
    
    ],
)
