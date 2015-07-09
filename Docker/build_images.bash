pushd gcc-5.1
docker build -t teeks99/gcc-5.1 .
popd
pushd clang-3.6
docker build -t teeks99/clang-3.6 .
popd
