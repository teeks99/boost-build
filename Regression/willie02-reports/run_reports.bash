cd /home/tomkent/willie02-reports
pushd boost
git pull
popd
boost/tools/regression/xsl_reports/build_results.sh develop
boost/tools/regression/xsl_reports/build_results.sh master

