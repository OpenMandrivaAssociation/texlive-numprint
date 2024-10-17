Name:		texlive-numprint
Version:	27498
Release:	2
Summary:	Print numbers with separators and exponent if necessary
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/numprint
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numprint.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numprint.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numprint.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package numprint prints numbers with a separator every
three digits and converts numbers given as 12345.6e789 to
12\,345,6\cdot 10^{789}. Numbers are printed in the current
mode (text or math) in order to use the correct font. Many
things, including the decimal sign, the thousand separator, as
well as the product sign can be changed by the user, e.g., to
reach 12,345.6\times 10^{789}. If an optional argument is given
it is printed upright as unit. Numbers can be rounded to a
given number of digits. The package supports an automatic,
language-dependent change of the number format. Tabular
alignment using the tabular(*), array, tabularx, and longtable
environments (similar to the dcolumn and rccol packages) is
supported using all features of numprint. Additional text can
be added before and after the formatted number.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/numprint/nbaseprt.sty
%{_texmfdistdir}/tex/latex/numprint/numprint.sty
%{_texmfdistdir}/tex/latex/numprint/numprint032.sty
%doc %{_texmfdistdir}/doc/latex/numprint/ChangeLog.nbaseprt
%doc %{_texmfdistdir}/doc/latex/numprint/ChangeLog.numprint
%doc %{_texmfdistdir}/doc/latex/numprint/Makefile
%doc %{_texmfdistdir}/doc/latex/numprint/README
%doc %{_texmfdistdir}/doc/latex/numprint/getversion.tex
%doc %{_texmfdistdir}/doc/latex/numprint/nbaseprt.pdf
%doc %{_texmfdistdir}/doc/latex/numprint/nbaseprttest.tex
%doc %{_texmfdistdir}/doc/latex/numprint/numprint.pdf
%doc %{_texmfdistdir}/doc/latex/numprint/numprinttest.tex
#- source
%doc %{_texmfdistdir}/source/latex/numprint/nbaseprt.dtx
%doc %{_texmfdistdir}/source/latex/numprint/numprint.dtx
%doc %{_texmfdistdir}/source/latex/numprint/numprint.ins
%doc %{_texmfdistdir}/source/latex/numprint/numprint032.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
