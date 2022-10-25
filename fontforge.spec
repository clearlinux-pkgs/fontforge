#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fontforge
Version  : 20220308
Release  : 34
URL      : https://github.com/fontforge/fontforge/archive/20220308/fontforge-20220308.tar.gz
Source0  : https://github.com/fontforge/fontforge/archive/20220308/fontforge-20220308.tar.gz
Summary  : A PostScript font editor
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0
Requires: fontforge-bin = %{version}-%{release}
Requires: fontforge-data = %{version}-%{release}
Requires: fontforge-lib = %{version}-%{release}
Requires: fontforge-license = %{version}-%{release}
Requires: fontforge-locales = %{version}-%{release}
Requires: fontforge-man = %{version}-%{release}
Requires: fontforge-python = %{version}-%{release}
Requires: fontforge-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : freetype-dev
BuildRequires : gettext-dev
BuildRequires : giflib-dev
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : libX11-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libspiro-dev
BuildRequires : libuninameslist
BuildRequires : libxml2-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(gdk-3.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libspiro)
BuildRequires : pkgconfig(libwoff2dec)
BuildRequires : pkgconfig(libwoff2enc)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(xrender)
BuildRequires : pypi(pillow)
BuildRequires : pypi-sphinx
BuildRequires : python3-dev
BuildRequires : readline-dev
BuildRequires : tiff-dev
BuildRequires : zlib-dev
Patch1: CVE-2017-17521.nopatch

%description
FontForge allows you to edit outline and bitmap fonts.  You can create
new ones or modify old ones.  It is also a font format converter and
can convert among PostScript (ASCII & binary Type 1, some Type 3s,
some Type 0s), TrueType, OpenType (Type2), CID-keyed and SVG fonts.

%package bin
Summary: bin components for the fontforge package.
Group: Binaries
Requires: fontforge-data = %{version}-%{release}
Requires: fontforge-license = %{version}-%{release}

%description bin
bin components for the fontforge package.


%package data
Summary: data components for the fontforge package.
Group: Data

%description data
data components for the fontforge package.


%package dev
Summary: dev components for the fontforge package.
Group: Development
Requires: fontforge-lib = %{version}-%{release}
Requires: fontforge-bin = %{version}-%{release}
Requires: fontforge-data = %{version}-%{release}
Provides: fontforge-devel = %{version}-%{release}
Requires: fontforge = %{version}-%{release}

%description dev
dev components for the fontforge package.


%package doc
Summary: doc components for the fontforge package.
Group: Documentation
Requires: fontforge-man = %{version}-%{release}

%description doc
doc components for the fontforge package.


%package lib
Summary: lib components for the fontforge package.
Group: Libraries
Requires: fontforge-data = %{version}-%{release}
Requires: fontforge-license = %{version}-%{release}

%description lib
lib components for the fontforge package.


%package license
Summary: license components for the fontforge package.
Group: Default

%description license
license components for the fontforge package.


%package locales
Summary: locales components for the fontforge package.
Group: Default

%description locales
locales components for the fontforge package.


%package man
Summary: man components for the fontforge package.
Group: Default

%description man
man components for the fontforge package.


%package python
Summary: python components for the fontforge package.
Group: Default
Requires: fontforge-python3 = %{version}-%{release}

%description python
python components for the fontforge package.


%package python3
Summary: python3 components for the fontforge package.
Group: Default
Requires: python3-core
Requires: pypi(pillow)

%description python3
python3 components for the fontforge package.


%prep
%setup -q -n fontforge-20220308
cd %{_builddir}/fontforge-20220308

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1646833862
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
%cmake .. -DENABLE_LIBUNINAMESLIST=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1646833862
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fontforge
cp %{_builddir}/fontforge-20220308/COPYING.gplv3 %{buildroot}/usr/share/package-licenses/fontforge/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/fontforge-20220308/LICENSE %{buildroot}/usr/share/package-licenses/fontforge/6e478823c3f8f96ffe2c3ae91ecddb2c0261c4b6
cp %{_builddir}/fontforge-20220308/Packaging/debian/cp-src/copyright %{buildroot}/usr/share/package-licenses/fontforge/8151e44930bd15f8056e01f399892c741b143f07
cp %{_builddir}/fontforge-20220308/doc/sphinx/olddocs/old/ja/license.html %{buildroot}/usr/share/package-licenses/fontforge/9149b619bc88b11d076a9416f1f21bffef7da963
pushd clr-build
%make_install
popd
%find_lang FontForge
## Remove excluded files
rm -f %{buildroot}*/usr/share/doc/fontforge/.buildinfo
rm -f %{buildroot}*/usr/share/doc/fontforge/.htaccess
rm -f %{buildroot}*/usr/share/doc/fontforge/.nojekyll

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fontforge
/usr/bin/fontimage
/usr/bin/fontlint
/usr/bin/sfddiff

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.fontforge.FontForge.desktop
/usr/share/fontforge/cidmap/Adobe-CNS1-6.cidmap
/usr/share/fontforge/cidmap/Adobe-GB1-5.cidmap
/usr/share/fontforge/cidmap/Adobe-Identity-0.cidmap
/usr/share/fontforge/cidmap/Adobe-Japan1-5.cidmap
/usr/share/fontforge/cidmap/Adobe-Japan1-6.cidmap
/usr/share/fontforge/cidmap/Adobe-Japan1-7.cidmap
/usr/share/fontforge/cidmap/Adobe-Japan2-0.cidmap
/usr/share/fontforge/cidmap/Adobe-Korea1-2.cidmap
/usr/share/fontforge/hotkeys/default
/usr/share/fontforge/pixmaps/Cantarell-Bold.ttf
/usr/share/fontforge/pixmaps/Cantarell-BoldOblique.ttf
/usr/share/fontforge/pixmaps/Cantarell-Oblique.ttf
/usr/share/fontforge/pixmaps/Cantarell-Regular.ttf
/usr/share/fontforge/pixmaps/Inconsolata-Bold.ttf
/usr/share/fontforge/pixmaps/Inconsolata-Regular.ttf
/usr/share/fontforge/pixmaps/OFL.txt
/usr/share/fontforge/pixmaps/changeweight.png
/usr/share/fontforge/pixmaps/charviewicon.xbm
/usr/share/fontforge/pixmaps/check_off.png
/usr/share/fontforge/pixmaps/check_off_disabled.png
/usr/share/fontforge/pixmaps/check_on.png
/usr/share/fontforge/pixmaps/check_on_disabled.png
/usr/share/fontforge/pixmaps/chooseraudio.png
/usr/share/fontforge/pixmaps/chooserback.png
/usr/share/fontforge/pixmaps/chooserbookmark.png
/usr/share/fontforge/pixmaps/choosercid.png
/usr/share/fontforge/pixmaps/choosercompressed.png
/usr/share/fontforge/pixmaps/chooserconfigtool.png
/usr/share/fontforge/pixmaps/choosercore.png
/usr/share/fontforge/pixmaps/chooserdir.png
/usr/share/fontforge/pixmaps/chooserforward.png
/usr/share/fontforge/pixmaps/chooserhomefolder.png
/usr/share/fontforge/pixmaps/chooserimage.png
/usr/share/fontforge/pixmaps/choosermac.png
/usr/share/fontforge/pixmaps/choosermacttf.png
/usr/share/fontforge/pixmaps/choosernobookmark.png
/usr/share/fontforge/pixmaps/chooserobject.png
/usr/share/fontforge/pixmaps/choosersfdir.png
/usr/share/fontforge/pixmaps/choosertar.png
/usr/share/fontforge/pixmaps/choosertextbdf.png
/usr/share/fontforge/pixmaps/choosertextc.png
/usr/share/fontforge/pixmaps/choosertextcss.png
/usr/share/fontforge/pixmaps/choosertextfontps.png
/usr/share/fontforge/pixmaps/choosertextfontsfd.png
/usr/share/fontforge/pixmaps/choosertexthtml.png
/usr/share/fontforge/pixmaps/choosertextjava.png
/usr/share/fontforge/pixmaps/choosertextmake.png
/usr/share/fontforge/pixmaps/choosertextplain.png
/usr/share/fontforge/pixmaps/choosertextps.png
/usr/share/fontforge/pixmaps/choosertextxml.png
/usr/share/fontforge/pixmaps/chooserttf.png
/usr/share/fontforge/pixmaps/chooserunknown.png
/usr/share/fontforge/pixmaps/chooserupdir.png
/usr/share/fontforge/pixmaps/chooservideo.png
/usr/share/fontforge/pixmaps/colorwheel.png
/usr/share/fontforge/pixmaps/downarrow.png
/usr/share/fontforge/pixmaps/downarrow_disabled.png
/usr/share/fontforge/pixmaps/editclear.png
/usr/share/fontforge/pixmaps/editclearback.png
/usr/share/fontforge/pixmaps/editcopy.png
/usr/share/fontforge/pixmaps/editcopyfg2bg.png
/usr/share/fontforge/pixmaps/editcopylayer2layer.png
/usr/share/fontforge/pixmaps/editcopylbearing.png
/usr/share/fontforge/pixmaps/editcopylookupdata.png
/usr/share/fontforge/pixmaps/editcopyrbearing.png
/usr/share/fontforge/pixmaps/editcopyref.png
/usr/share/fontforge/pixmaps/editcopyvwidth.png
/usr/share/fontforge/pixmaps/editcopywidth.png
/usr/share/fontforge/pixmaps/editcut.png
/usr/share/fontforge/pixmaps/editfind.png
/usr/share/fontforge/pixmaps/editjoin.png
/usr/share/fontforge/pixmaps/editmerge.png
/usr/share/fontforge/pixmaps/editmergetoline.png
/usr/share/fontforge/pixmaps/editpaste.png
/usr/share/fontforge/pixmaps/editpasteafter.png
/usr/share/fontforge/pixmaps/editpasteinto.png
/usr/share/fontforge/pixmaps/editredo.png
/usr/share/fontforge/pixmaps/editrmundoes.png
/usr/share/fontforge/pixmaps/editrplref.png
/usr/share/fontforge/pixmaps/editsameas.png
/usr/share/fontforge/pixmaps/editselect.png
/usr/share/fontforge/pixmaps/editundo.png
/usr/share/fontforge/pixmaps/editunlink.png
/usr/share/fontforge/pixmaps/elementaddextrema.png
/usr/share/fontforge/pixmaps/elementaddinflections.png
/usr/share/fontforge/pixmaps/elementalign.png
/usr/share/fontforge/pixmaps/elementanticlock.png
/usr/share/fontforge/pixmaps/elementautotrace.png
/usr/share/fontforge/pixmaps/elementbalance.png
/usr/share/fontforge/pixmaps/elementbdfinfo.png
/usr/share/fontforge/pixmaps/elementbitmapsavail.png
/usr/share/fontforge/pixmaps/elementbuildaccent.png
/usr/share/fontforge/pixmaps/elementbuildcomposite.png
/usr/share/fontforge/pixmaps/elementclockwise.png
/usr/share/fontforge/pixmaps/elementcomparefonts.png
/usr/share/fontforge/pixmaps/elementcomparelayers.png
/usr/share/fontforge/pixmaps/elementcorrectdir.png
/usr/share/fontforge/pixmaps/elementexpandstroke.png
/usr/share/fontforge/pixmaps/elementfindprobs.png
/usr/share/fontforge/pixmaps/elementfontinfo.png
/usr/share/fontforge/pixmaps/elementgetinfo.png
/usr/share/fontforge/pixmaps/elementglyphinfo.png
/usr/share/fontforge/pixmaps/elementharmonize.png
/usr/share/fontforge/pixmaps/elementhbaselines.png
/usr/share/fontforge/pixmaps/elementinterpolatefonts.png
/usr/share/fontforge/pixmaps/elementmathinfo.png
/usr/share/fontforge/pixmaps/elementmergefonts.png
/usr/share/fontforge/pixmaps/elementorder.png
/usr/share/fontforge/pixmaps/elementotherinfo.png
/usr/share/fontforge/pixmaps/elementregenbitmaps.png
/usr/share/fontforge/pixmaps/elementremovebitmaps.png
/usr/share/fontforge/pixmaps/elementrenameglyph.png
/usr/share/fontforge/pixmaps/elementround.png
/usr/share/fontforge/pixmaps/elementshowdep.png
/usr/share/fontforge/pixmaps/elementsimplify.png
/usr/share/fontforge/pixmaps/elementstyles.png
/usr/share/fontforge/pixmaps/elementtilepath.png
/usr/share/fontforge/pixmaps/elementtilepattern.png
/usr/share/fontforge/pixmaps/elementtransform.png
/usr/share/fontforge/pixmaps/elementvalidate.png
/usr/share/fontforge/pixmaps/elementvbaselines.png
/usr/share/fontforge/pixmaps/exclude.png
/usr/share/fontforge/pixmaps/extendcondense.png
/usr/share/fontforge/pixmaps/fflogo.png
/usr/share/fontforge/pixmaps/fflogo13.png
/usr/share/fontforge/pixmaps/ffsplash1.png
/usr/share/fontforge/pixmaps/ffsplash2.png
/usr/share/fontforge/pixmaps/ffsplash3.png
/usr/share/fontforge/pixmaps/fileclose.png
/usr/share/fontforge/pixmaps/fileclose2.png
/usr/share/fontforge/pixmaps/filedisplay.png
/usr/share/fontforge/pixmaps/fileexecute.png
/usr/share/fontforge/pixmaps/fileexport.png
/usr/share/fontforge/pixmaps/filegenerate.png
/usr/share/fontforge/pixmaps/filegeneratefamily.png
/usr/share/fontforge/pixmaps/fileimport.png
/usr/share/fontforge/pixmaps/filemergefeature.png
/usr/share/fontforge/pixmaps/filenew.png
/usr/share/fontforge/pixmaps/fileopen.png
/usr/share/fontforge/pixmaps/fileprefs.png
/usr/share/fontforge/pixmaps/fileprint.png
/usr/share/fontforge/pixmaps/filequit.png
/usr/share/fontforge/pixmaps/filerecent.png
/usr/share/fontforge/pixmaps/filerevert.png
/usr/share/fontforge/pixmaps/filerevertbackup.png
/usr/share/fontforge/pixmaps/filerevertglyph.png
/usr/share/fontforge/pixmaps/filesave.png
/usr/share/fontforge/pixmaps/filesaveall.png
/usr/share/fontforge/pixmaps/filesaveas.png
/usr/share/fontforge/pixmaps/findinter.png
/usr/share/fontforge/pixmaps/fliphor.png
/usr/share/fontforge/pixmaps/flipvert.png
/usr/share/fontforge/pixmaps/fontview2.xbm
/usr/share/fontforge/pixmaps/helpabout.png
/usr/share/fontforge/pixmaps/helphelp.png
/usr/share/fontforge/pixmaps/helpindex.png
/usr/share/fontforge/pixmaps/hintsadddstem.png
/usr/share/fontforge/pixmaps/hintsaddhstem.png
/usr/share/fontforge/pixmaps/hintsaddvstem.png
/usr/share/fontforge/pixmaps/hintsautohint.png
/usr/share/fontforge/pixmaps/hintscleardstems.png
/usr/share/fontforge/pixmaps/hintsclearhstems.png
/usr/share/fontforge/pixmaps/hintsclearvstems.png
/usr/share/fontforge/pixmaps/hintsdontautohint.png
/usr/share/fontforge/pixmaps/hintsreviewhints.png
/usr/share/fontforge/pixmaps/inline.png
/usr/share/fontforge/pixmaps/intersection.png
/usr/share/fontforge/pixmaps/logo.xbm
/usr/share/fontforge/pixmaps/menuempty.png
/usr/share/fontforge/pixmaps/metricscenter.png
/usr/share/fontforge/pixmaps/metricssetlbearing.png
/usr/share/fontforge/pixmaps/metricssetrbearing.png
/usr/share/fontforge/pixmaps/metricssetvwidth.png
/usr/share/fontforge/pixmaps/metricssetwidth.png
/usr/share/fontforge/pixmaps/oblique.png
/usr/share/fontforge/pixmaps/outline.png
/usr/share/fontforge/pixmaps/overlapexclude.png
/usr/share/fontforge/pixmaps/overlapfindinter.png
/usr/share/fontforge/pixmaps/overlapintersection.png
/usr/share/fontforge/pixmaps/overlaprm.png
/usr/share/fontforge/pixmaps/palette3drotate-selected.png
/usr/share/fontforge/pixmaps/palette3drotate.png
/usr/share/fontforge/pixmaps/palettecorner-selected.png
/usr/share/fontforge/pixmaps/palettecorner.png
/usr/share/fontforge/pixmaps/palettecurve-selected.png
/usr/share/fontforge/pixmaps/palettecurve.png
/usr/share/fontforge/pixmaps/paletteelipse-selected.png
/usr/share/fontforge/pixmaps/paletteelipse.png
/usr/share/fontforge/pixmaps/paletteflip-selected.png
/usr/share/fontforge/pixmaps/paletteflip.png
/usr/share/fontforge/pixmaps/palettefreehand-selected.png
/usr/share/fontforge/pixmaps/palettefreehand.png
/usr/share/fontforge/pixmaps/palettehand-selected.png
/usr/share/fontforge/pixmaps/palettehand.png
/usr/share/fontforge/pixmaps/palettehvcurve-selected.png
/usr/share/fontforge/pixmaps/palettehvcurve.png
/usr/share/fontforge/pixmaps/paletteknife-selected.png
/usr/share/fontforge/pixmaps/paletteknife.png
/usr/share/fontforge/pixmaps/paletteline.png
/usr/share/fontforge/pixmaps/palettemagnify-selected.png
/usr/share/fontforge/pixmaps/palettemagnify.png
/usr/share/fontforge/pixmaps/palettepen-selected.png
/usr/share/fontforge/pixmaps/palettepen.png
/usr/share/fontforge/pixmaps/palettepencil.png
/usr/share/fontforge/pixmaps/paletteperspective-selected.png
/usr/share/fontforge/pixmaps/paletteperspective.png
/usr/share/fontforge/pixmaps/palettepointer-selected.png
/usr/share/fontforge/pixmaps/palettepointer.png
/usr/share/fontforge/pixmaps/palettepoly-selected.png
/usr/share/fontforge/pixmaps/palettepoly.png
/usr/share/fontforge/pixmaps/paletterect-selected.png
/usr/share/fontforge/pixmaps/paletterect.png
/usr/share/fontforge/pixmaps/paletterotate-selected.png
/usr/share/fontforge/pixmaps/paletterotate.png
/usr/share/fontforge/pixmaps/paletteruler-selected.png
/usr/share/fontforge/pixmaps/paletteruler.png
/usr/share/fontforge/pixmaps/palettescale-selected.png
/usr/share/fontforge/pixmaps/palettescale.png
/usr/share/fontforge/pixmaps/paletteselectedbg.png
/usr/share/fontforge/pixmaps/paletteshift.png
/usr/share/fontforge/pixmaps/paletteskew-selected.png
/usr/share/fontforge/pixmaps/paletteskew.png
/usr/share/fontforge/pixmaps/palettesmall3drotate.png
/usr/share/fontforge/pixmaps/palettesmallcorner.png
/usr/share/fontforge/pixmaps/palettesmallcurve.png
/usr/share/fontforge/pixmaps/palettesmallelipse.png
/usr/share/fontforge/pixmaps/palettesmallflip.png
/usr/share/fontforge/pixmaps/palettesmallhand.png
/usr/share/fontforge/pixmaps/palettesmallhvcurve.png
/usr/share/fontforge/pixmaps/palettesmallknife.png
/usr/share/fontforge/pixmaps/palettesmallmag.png
/usr/share/fontforge/pixmaps/palettesmallpen.png
/usr/share/fontforge/pixmaps/palettesmallpencil.png
/usr/share/fontforge/pixmaps/palettesmallperspective.png
/usr/share/fontforge/pixmaps/palettesmallpointer.png
/usr/share/fontforge/pixmaps/palettesmallpoly.png
/usr/share/fontforge/pixmaps/palettesmallrect.png
/usr/share/fontforge/pixmaps/palettesmallrotate.png
/usr/share/fontforge/pixmaps/palettesmallruler.png
/usr/share/fontforge/pixmaps/palettesmallscale.png
/usr/share/fontforge/pixmaps/palettesmallskew.png
/usr/share/fontforge/pixmaps/palettesmallspirocorner.png
/usr/share/fontforge/pixmaps/palettesmallspirocurve.png
/usr/share/fontforge/pixmaps/palettesmallspirog2curve.png
/usr/share/fontforge/pixmaps/palettesmallspiroleft.png
/usr/share/fontforge/pixmaps/palettesmallspiroright.png
/usr/share/fontforge/pixmaps/palettesmallstar.png
/usr/share/fontforge/pixmaps/palettesmalltangent.png
/usr/share/fontforge/pixmaps/palettespirocorner-selected.png
/usr/share/fontforge/pixmaps/palettespirocorner.png
/usr/share/fontforge/pixmaps/palettespirocurve-selected.png
/usr/share/fontforge/pixmaps/palettespirocurve.png
/usr/share/fontforge/pixmaps/palettespirodisabled.png
/usr/share/fontforge/pixmaps/palettespirodown.png
/usr/share/fontforge/pixmaps/palettespirog2curve-selected.png
/usr/share/fontforge/pixmaps/palettespirog2curve.png
/usr/share/fontforge/pixmaps/palettespiroleft-selected.png
/usr/share/fontforge/pixmaps/palettespiroleft.png
/usr/share/fontforge/pixmaps/palettespiroright-selected.png
/usr/share/fontforge/pixmaps/palettespiroright.png
/usr/share/fontforge/pixmaps/palettespiroup-selected.png
/usr/share/fontforge/pixmaps/palettespiroup.png
/usr/share/fontforge/pixmaps/palettestar-selected.png
/usr/share/fontforge/pixmaps/palettestar.png
/usr/share/fontforge/pixmaps/palettetangent-selected.png
/usr/share/fontforge/pixmaps/palettetangent.png
/usr/share/fontforge/pixmaps/pointsG2curve.png
/usr/share/fontforge/pixmaps/pointsaddanchor.png
/usr/share/fontforge/pixmaps/pointscorner.png
/usr/share/fontforge/pixmaps/pointscurve.png
/usr/share/fontforge/pixmaps/pointshvcurve.png
/usr/share/fontforge/pixmaps/pointsmakearc.png
/usr/share/fontforge/pixmaps/pointsmakeline.png
/usr/share/fontforge/pixmaps/pointsnamecontour.png
/usr/share/fontforge/pixmaps/pointsnamepoint.png
/usr/share/fontforge/pixmaps/pointsspironext.png
/usr/share/fontforge/pixmaps/pointsspiroprev.png
/usr/share/fontforge/pixmaps/pointstangent.png
/usr/share/fontforge/pixmaps/ptinfocorner.png
/usr/share/fontforge/pixmaps/ptinfocurve.png
/usr/share/fontforge/pixmaps/ptinfohvcurve.png
/usr/share/fontforge/pixmaps/ptinfotangent.png
/usr/share/fontforge/pixmaps/python.png
/usr/share/fontforge/pixmaps/radio_off.png
/usr/share/fontforge/pixmaps/radio_off_disabled.png
/usr/share/fontforge/pixmaps/radio_on.png
/usr/share/fontforge/pixmaps/radio_on_disabled.png
/usr/share/fontforge/pixmaps/resources
/usr/share/fontforge/pixmaps/rmoverlap.png
/usr/share/fontforge/pixmaps/rotate180.png
/usr/share/fontforge/pixmaps/rotateccw.png
/usr/share/fontforge/pixmaps/rotatecw.png
/usr/share/fontforge/pixmaps/selectblue.png
/usr/share/fontforge/pixmaps/selectcyan.png
/usr/share/fontforge/pixmaps/selectdefault.png
/usr/share/fontforge/pixmaps/selectgreen.png
/usr/share/fontforge/pixmaps/selectmagenta.png
/usr/share/fontforge/pixmaps/selectred.png
/usr/share/fontforge/pixmaps/selectwhite.png
/usr/share/fontforge/pixmaps/selectyellow.png
/usr/share/fontforge/pixmaps/shadow.png
/usr/share/fontforge/pixmaps/skew.png
/usr/share/fontforge/pixmaps/splash2019.png
/usr/share/fontforge/pixmaps/splash2020.png
/usr/share/fontforge/pixmaps/styleschangeweight.png
/usr/share/fontforge/pixmaps/styleschangexheight.png
/usr/share/fontforge/pixmaps/stylesextendcondense.png
/usr/share/fontforge/pixmaps/stylesinline.png
/usr/share/fontforge/pixmaps/stylesitalic.png
/usr/share/fontforge/pixmaps/stylesoblique.png
/usr/share/fontforge/pixmaps/stylesoutline.png
/usr/share/fontforge/pixmaps/stylesshadow.png
/usr/share/fontforge/pixmaps/stylessmallcaps.png
/usr/share/fontforge/pixmaps/stylessubsuper.png
/usr/share/fontforge/pixmaps/styleswireframe.png
/usr/share/fontforge/pixmaps/text12210.png
/usr/share/fontforge/pixmaps/tools3drotate.png
/usr/share/fontforge/pixmaps/toolselipse.png
/usr/share/fontforge/pixmaps/toolsflip.png
/usr/share/fontforge/pixmaps/toolsfreehand.png
/usr/share/fontforge/pixmaps/toolsknife.png
/usr/share/fontforge/pixmaps/toolsmagnify.png
/usr/share/fontforge/pixmaps/toolspen.png
/usr/share/fontforge/pixmaps/toolsperspective.png
/usr/share/fontforge/pixmaps/toolspointer.png
/usr/share/fontforge/pixmaps/toolspolygon.png
/usr/share/fontforge/pixmaps/toolsrect.png
/usr/share/fontforge/pixmaps/toolsrotate.png
/usr/share/fontforge/pixmaps/toolsruler.png
/usr/share/fontforge/pixmaps/toolsscale.png
/usr/share/fontforge/pixmaps/toolsscroll.png
/usr/share/fontforge/pixmaps/toolsskew.png
/usr/share/fontforge/pixmaps/toolsspiro.png
/usr/share/fontforge/pixmaps/toolsstar.png
/usr/share/fontforge/pixmaps/transformfliphor.png
/usr/share/fontforge/pixmaps/transformflipvert.png
/usr/share/fontforge/pixmaps/transformrotate180.png
/usr/share/fontforge/pixmaps/transformrotateccw.png
/usr/share/fontforge/pixmaps/transformrotatecw.png
/usr/share/fontforge/pixmaps/transformskew.png
/usr/share/fontforge/pixmaps/ttdebugcontinue.png
/usr/share/fontforge/pixmaps/ttdebugexit.png
/usr/share/fontforge/pixmaps/ttdebugmenudelta.png
/usr/share/fontforge/pixmaps/ttdebugstepinto.png
/usr/share/fontforge/pixmaps/ttdebugstepout.png
/usr/share/fontforge/pixmaps/ttdebugstepover.png
/usr/share/fontforge/pixmaps/ttdebugstop.png
/usr/share/fontforge/pixmaps/ttdebugstopped.png
/usr/share/fontforge/pixmaps/ttdebugwatchpnt.png
/usr/share/fontforge/pixmaps/viewbiggersize.png
/usr/share/fontforge/pixmaps/viewfindinfont.png
/usr/share/fontforge/pixmaps/viewfit.png
/usr/share/fontforge/pixmaps/viewformer.png
/usr/share/fontforge/pixmaps/viewgoto.png
/usr/share/fontforge/pixmaps/viewinsertafter.png
/usr/share/fontforge/pixmaps/viewinsertbefore.png
/usr/share/fontforge/pixmaps/viewlayers.png
/usr/share/fontforge/pixmaps/viewnext.png
/usr/share/fontforge/pixmaps/viewnextdef.png
/usr/share/fontforge/pixmaps/viewpalettes.png
/usr/share/fontforge/pixmaps/viewprev.png
/usr/share/fontforge/pixmaps/viewprevdef.png
/usr/share/fontforge/pixmaps/viewreplace.png
/usr/share/fontforge/pixmaps/viewsmallersize.png
/usr/share/fontforge/pixmaps/viewzoomin.png
/usr/share/fontforge/pixmaps/viewzoomout.png
/usr/share/fontforge/pixmaps/wireframe.png
/usr/share/fontforge/prefs
/usr/share/fontforge/python/excepthook.py
/usr/share/icons/hicolor/128x128/apps/org.fontforge.FontForge.png
/usr/share/icons/hicolor/16x16/apps/org.fontforge.FontForge.png
/usr/share/icons/hicolor/22x22/apps/org.fontforge.FontForge.png
/usr/share/icons/hicolor/24x24/apps/org.fontforge.FontForge.png
/usr/share/icons/hicolor/256x256/apps/org.fontforge.FontForge.png
/usr/share/icons/hicolor/32x32/apps/org.fontforge.FontForge.png
/usr/share/icons/hicolor/48x48/apps/org.fontforge.FontForge.png
/usr/share/icons/hicolor/512x512/apps/org.fontforge.FontForge.png
/usr/share/icons/hicolor/64x64/apps/org.fontforge.FontForge.png
/usr/share/icons/hicolor/scalable/apps/org.fontforge.FontForge.svg
/usr/share/metainfo/org.fontforge.FontForge.appdata.xml
/usr/share/mime-packages/fontforge.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/libfontforge.so

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/fontforge/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfontforge.so.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fontforge/6e478823c3f8f96ffe2c3ae91ecddb2c0261c4b6
/usr/share/package-licenses/fontforge/8151e44930bd15f8056e01f399892c741b143f07
/usr/share/package-licenses/fontforge/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/fontforge/9149b619bc88b11d076a9416f1f21bffef7da963

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fontforge.1
/usr/share/man/man1/fontimage.1
/usr/share/man/man1/fontlint.1
/usr/share/man/man1/sfddiff.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f FontForge.lang
%defattr(-,root,root,-)

