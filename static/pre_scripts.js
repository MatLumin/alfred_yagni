


async function get_data_of_image_collection(uti)
	{
	let response = await fetch(`/get_image_collection_data?uti=${uti}`);
	let json = await response.json();
	return json["data"];
	}


function update_image(text_holder, image_holder, images, state)
	{
	let image_count = images.length;
	let current_image= images[state.last_index].data;
	let current_text = images[state.last_index].title;
	text_holder.innerText = current_text;
	image_holder.src = current_image;
	state.last_index += 1;
	state.last_index = state.last_index % image_count;
	}


async function handle_image_collection(id_of_image_holder, id_of_text_holder, uti)
	{
	let data = await get_data_of_image_collection(uti);
	console.log(data);
	let images = data["images"];
	let state = {"last_index":0,}

	let text_holder = document.getElementById(id_of_text_holder);
	let image_holder = document.getElementById(id_of_image_holder);



	setInterval(
		function() 
			{
			update_image(text_holder, image_holder, images, state)
			},

		1000)
	}