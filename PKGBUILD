pkgname=dowtube
pkgver=1.0
pkgrel=2
pkgdesc="a simple youtube audio-video dowloader"
arch=('any')
url="https://github.com/BlackSnaker/DowTube"
license=('GPL')
makedepends=('git')
depends=('python-pytube' 'python-pyqt6')
source=("git+https://github.com/BlackSnaker/DowTube")
sha256sums=('SKIP')

package() {
    install -Dm644 "$srcdir/DowTube/youtube.png" "${pkgdir}/usr/share/pixmaps/dowtube.png"
    install -Dm644 "$srcdir/DowTube/DowTube.desktop" "${pkgdir}/usr/share/applications/dowtube.png"
    install -Dm755 "$srcdir/DowTube/DowTube.py" "${pkgdir}/usr/bin/dowtube"
}

