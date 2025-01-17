Name:		texlive-beamer-tut-pt
Version:	15878
Release:	2
Summary:	An introduction to the Beamer class, in Portuguese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/portuguese/beamer
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-tut-pt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-tut-pt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive beamer-tut-pt package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/AnnArbor1.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/AnnArbor2.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/CambridgeUS1.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/CambridgeUS2.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/LEIAME
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/README
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/anim1.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/anim2.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/anim3.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/anim4.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/automato1.jpg
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/automato2.jpg
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/automato3.jpg
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/automato4.jpg
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/automato5.jpg
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/berkeley1.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/berkeley2.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/blocos.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/boadilla1.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/boadilla2.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/exemplo.tex
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/madrid1.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/madrid2.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/montpellier1.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/montpellier2.ps
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/tutorialbeamer.pdf
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/tutorialbeamer.tex
%doc %{_texmfdistdir}/doc/latex/beamer-tut-pt/ufpellogo.jpg

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
