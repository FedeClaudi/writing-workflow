for entry in "scripts"/*
do
    echo "Running scripts/$entry"
    python $entry
done