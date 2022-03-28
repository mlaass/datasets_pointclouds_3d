function process()
{
    echo "convert $1 -> ${1%.*}.off"
    ctmconv "$1"  "${1%.*}.off" --no-colors  --no-normals 
}
export -f process
find $1 -name $2   | parallel process {}
