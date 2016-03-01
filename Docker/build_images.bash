
for compiler in gcc-4.4 gcc-4.5 gcc-4.6 gcc-4.7 gcc-4.8 gcc-4.9 gcc-5 clang-2.9 clang-3.0 clang-3.1 clang-3.2 clang-3.3 clang-3.4 clang-3.5 clang-3.6 clang-3.7
do
  pushd $compiler
  echo docker build -t teeks99/$compiler .
  docker build -t teeks99/$compiler .
  popd
done

