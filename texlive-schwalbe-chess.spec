# revision 29941
# category Package
# catalog-ctan /macros/latex/contrib/schwalbe-chess
# catalog-date 2013-04-14 18:39:07 +0200
# catalog-license lppl1.2
# catalog-version 1.5.1
Name:		texlive-schwalbe-chess
Version:	1.5.1
Release:	8
Summary:	Typeset the German chess magazine "Die Schwalbe"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/schwalbe-chess
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schwalbe-chess.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schwalbe-chess.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schwalbe-chess.source.tar.xz
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
%{_texmfdistdir}/tex/latex/schwalbe-chess/schwalbe.cls
%{_texmfdistdir}/tex/latex/schwalbe-chess/schwalbe.sty
%doc %{_texmfdistdir}/doc/latex/schwalbe-chess/README
%doc %{_texmfdistdir}/doc/latex/schwalbe-chess/schwalbe.pdf
#- source
%doc %{_texmfdistdir}/source/latex/schwalbe-chess/schwalbe.dtx
%doc %{_texmfdistdir}/source/latex/schwalbe-chess/schwalbe.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
