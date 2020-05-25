# install

## OpenCV

관련없고 필요없는 패키지 제거
```
$sudo apt-get purge wolfram-engine
$sudo apt-get purge libreoffice*
$sudo apt-get clean
$sudo apt-get autoremove

```

업그레이드 및 기본 개발 도구
```
$sudo apt-get update&& sudo apt-get upgrade
$sudo apt-get install build-essential cmake unzip pkg-config
```

이미지 관련 라이브러리 설치
비디오 관련 라이브러리와 코덱 라이브러리 설치
```
$sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
$sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
$sudo apt-get install libxvidcore-dev libx264-dev
```

OpenCV GUI를 위한 GTK or QT GUI 백엔드 선택
```
$sudo apt-get install libgtk-3-dev
$sudo apt-get install libcanberra-gtk*
```

이미지 처리 위한 라이브러리와 파이썬 라이브러리
```
$sudo apt-get install libatlas-base-dev gfortran
$sudo apt-get install python3-dev
```

NumPy설치
```
$sudo apt install python-numpy python3-numpy
```

Download opencv 4 for raspberry pi
```
$cd~
$wget -O opencv.zip https://github.com/opencv/opencv/archive/4.1.1.zip
$wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.1.1.zip
$unzip opencv.zip
$unzip opencv_contrib.zip
```

CMake and compile
```
$cd ~/opencv-4.1.1
$mkdir build
$cd build

$pwd
~/opencv-4.1.1/build
$cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D OPENCV_EXTRA_MODULES_PATH = ~/opencv_contib-4.1.1/modules \
-D ENABLE_NEON=ON \
-D ENABLE_VFPV3=ON \
-D BUILD_TESTS=OFF \
-D OPENCV_ENABLE_NONFREE=ON \
-D INSTALL_PYTHON_EXAMPLES=OFF \
-D CMAKE_SHARED_LINKER_FLAGS='-latomic' \
-D BUILD_EXAMPLES=OFF ..
```

이건 뭔지 모르겠음 이걸로 해야되는건가.
```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-4.1.1/modules \
-D ENABLE_NEON=ON \
-D ENABLE_VFPV3=ON \
-D BUILD_TESTS=OFF \
-D OPENCV_ENABLE_NONFREE=ON \
-D INSTALL_PYTHON_EXAMPLES=OFF \
-D CMAKE_SHARED_LINKER_FLAGS='-latomic' \
-D WITH_QT=OFF -D WITH_GTK=ON \
-D BUILD_EXAMPLES=OFF ..
```

스왑공간 늘리기
CONF_SWAPSIZE변수값을 100에서 2048로 수정
```
$sudo vim /etc/dphys-swapfile
```
```
#you most likely don't want this, unless you have an special disk situation
#CONF_SWAPSIZE=100
CONF_SWAPSIZE=2048
```
dpyhs-swapfile service 재시작
```
$sudo systemctl restart dphys-swapfile.service
```

build 디렉토리에서 컴파일
```
$make -j4
$sudo make install
```
스왑 공간은 다시 100으로 돌려놓는다.(위에서 했던 과정 다시)

설치 완료되면 import cv2로 확인해 볼 수 있다.
사용이 되지 않는다면 경로를 추가한다.
```
$sudo sh -c 'echo "/usr/local/lib">>/etc/ld.so.conf/opencv.conf'
$sudo ldconfig
```

## conda
conda 설치
```
$wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
$sh Anaconda3-2020.02-Linux-x86_64.sh
```

conda init이 자동으로 되지 않은 경우
```
$./anaconda3/bin/conda init
```

conda 가상환경 생성 및 활성화
```
$conda create -n opencv4 numpy matplotlib
$conda activate opencv4
```

??설치??
```
$conda install -c conda-forge opencv
```
(...나중에 계속


#### cv2.imread(fileName, flag)




-----
ls -l /dev/vide0 이 있으면 잘 연결되었다는 뜻.
cap = cv2.VideoCapture(0)하면 0번째(기본으로 설정된) 카메라로 잡음.

/usr/local/share/opencv4/haarcascades
~/anaconda3/envs/[가상환경 ]/share/opencv4/haarcascades
