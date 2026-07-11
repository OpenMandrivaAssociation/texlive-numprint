%global tl_name numprint
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.39
Release:	%{tl_revision}.1
Summary:	Print numbers with separators and exponent if necessary
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/numprint
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/numprint.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/numprint.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/numprint.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package numprint prints numbers with a separator every three digits
and converts numbers given as 12345.6e789 to 12\,345,6\cdot 10^{789}.
Numbers are printed in the current mode (text or math) in order to use
the correct font. Many things, including the decimal sign, the thousand
separator, as well as the product sign can be changed by the user, e.g.,
to reach 12,345.6\times 10^{789}. If an optional argument is given it is
printed upright as unit. Numbers can be rounded to a given number of
digits. The package supports an automatic, language-dependent change of
the number format. Tabular alignment using the tabular(*), array,
tabularx, and longtable environments (similar to the dcolumn and rccol
packages) is supported using all features of numprint. Additional text
can be added before and after the formatted number.

