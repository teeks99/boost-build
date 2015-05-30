#for ver in a b c d e f g h i n o p q r s t u v
for ver in a b
do
   cd $ver
   rm -rf boost_root
   rm -rf results
   rm -rf boost_bb
   rm -rf boost_regression
   rm -rf boost_regression_src
   cd ..
done
