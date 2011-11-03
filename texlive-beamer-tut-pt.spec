# revision 15878
# category Package
# catalog-ctan /info/portuguese/beamer
# catalog-date 2007-03-05 14:17:42 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-beamer-tut-pt
Version:	20070305
Release:	1
Summary:	An introduction to the Beamer class, in Portuguese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/portuguese/beamer
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-tut-pt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-tut-pt.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
