for i  in *.mp3; do
	#Extract relevant names for Artist and Song and remove any leading and trailing whitespace
	artistName="$(echo -e "${i}" | cut -d'-' -f 1 | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"
    #file name of (print if file in i exist, with that cut the file name that is separated by -)
    #with that we replace the text that exist from - to /
	songName="$(echo -e "${i}" | cut -d'-' -f 2 | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"

	mkdir -p "$artistName" #Create the directory only if it does not already exist
  mv "$i" "$artistName//$songName" #Move the files into the directory
done

