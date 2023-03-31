Name:		texlive-schwalbe-chess
Version:	63708
Release:	2
Summary:	Typeset the German chess magazine "Die Schwalbe"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/schwalbe-chess
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schwalbe-chess.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schwalbe-chess.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schwalbe-chess.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is based on chess-problem-diagrams, which in its
turn has a dependency on the bartel-chess-fonts.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/schwalbe-chess
%doc %{_texmfdistdir}/doc/latex/schwalbe-chess
#- source
%doc %{_texmfdistdir}/source/latex/schwalbe-chess

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
