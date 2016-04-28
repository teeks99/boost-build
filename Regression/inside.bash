cd /var/boost

group_id=$(stat -c '%g' CurrentRun.json)
user_id=$(stat -c '%u' CurrentRun.json)

echo addgroup --gid=$group_id boost
addgroup --gid=$group_id boost
echo adduser --disabled-password --ingroup boost --gecos "" boost
adduser --disabled-password --ingroup boost --gecos "" boost

cp /user-config.jam /home/boost/
su boost -c "python2.7 /var/boost/single.py"
