Name:           fmod-engine
Version:        2.02.22
Release:        1%{?dist}
Summary:        Made for games - FMOD is the solution for adaptive audio.

License:        FMOD
URL:            https://www.fmod.com/
Source0:        fmodstudioapi20222linux.tar.gz

BuildRequires:	coreutils
Requires:	coreutils

%description
Made for games - FMOD is the solution for adaptive audio.

%package plugins
Requires: coreutils
Summary: Made for games - FMOD is the solution for adaptive audio.

%description plugins
Made for games - FMOD is the solution for adaptive audio.

%package bin
Requires: coreutils, fmod-engine, fmod-engine-plugins, fmod-engine-doc, fmod-engine-api-studio, fmod-engine-api-core, fmod-engine-api-fsbank
Summary: Made for games - FMOD is the solution for adaptive audio.

%description bin
Made for games - FMOD is the solution for adaptive audio.

%package doc
Requires: coreutils 
Summary: Made for games - FMOD is the solution for adaptive audio.

%description doc
Made for games - FMOD is the solution for adaptive audio.

%package api-studio
Requires: coreutils 
Summary: Made for games - FMOD is the solution for adaptive audio.

%description api-studio
Made for games - FMOD is the solution for adaptive audio.

%package api-core
Requires: coreutils 
Summary: Made for games - FMOD is the solution for adaptive audio.

%description api-core
Made for games - FMOD is the solution for adaptive audio.

%package api-fsbank
Requires: coreutils, libvorbis-devel
Summary: Made for games - FMOD is the solution for adaptive audio.

%description api-fsbank
Made for games - FMOD is the solution for adaptive audio.
