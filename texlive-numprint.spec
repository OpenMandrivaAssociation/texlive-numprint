# revision 27498
# category Package
# catalog-ctan /macros/latex/contrib/numprint
# catalog-date 2012-08-22 15:46:20 +0200
# catalog-license lppl
# catalog-version 1.39
Name:		texlive-numprint
Version:	1.39
Release:	7
Summary:	Print numbers with separators and exponent if necessary
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/numprint
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numprint.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numprint.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numprint.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Oct 29 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.39-1
+ Revision: 820521
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.38-2
+ Revision: 754450
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.38-1
+ Revision: 719145
- texlive-numprint
- texlive-numprint
- texlive-numprint
- texlive-numprint

