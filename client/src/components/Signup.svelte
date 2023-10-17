<script>
	export let togglesignIn;

	let data = {
		full_name: '',
		email: '',
		phone_number: '',
		referral_code: '',
		password: ''
	};

	function handleKeyDown(event) {
		if (event.keyCode == 'Enter') {
			return handleSubmit();
		}
	}
	async function handleSubmit() {
		// Create a JSON object containing the data

		const requestData = JSON.stringify(data);

		// Specify the URL to send the POST request to
		const url = 'https://raj74434.pythonanywhere.com/signUp';

		try {
			const response = await fetch(url, {
				method: 'POST',
				body: requestData,
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (response.ok) {
				console.log('Request was successful');
				console.log(response);
				// You can redirect or handle the response as needed here
			} else {
				console.error('Failed', 'Request failed');
			}
		} catch (error) {
			console.error('Error:', error);
		}
	}
	$: {
		console.log(data);
	}
</script>

<main class=" flex flex-col gap-3">
	<div class="text-center">
		<h1 class="text-3xl font-medium">Create Account</h1>
		<p class="text-lg font-medium">
			Already have an account? <span
				class="text-[#4358F6] hover:underline hover:cursor-pointer"
				on:click={togglesignIn}
				on:keydown={handleKeyDown}
				tabindex="0"
				role="button">Sign In</span
			>
		</p>
	</div>

	<div class="flex flex-col gap-4">
		<div>
			<p>Full Name <span class="text-[#ff3561]">*</span></p>
			<input
				class="border border-1 border-[#f0f4f7] rounded-lg h-12 w-full px-2"
				type="text"
				placeholder="Enter your Full name"
				bind:value={data.full_name}
			/>
		</div>
		<div>
			<p>Email address <span class="text-[#ff3561]">*</span></p>
			<input
				class="border border-1 border-[#f0f4f7] rounded-lg h-12 w-full px-2"
				type="text"
				placeholder="Enter email address"
				bind:value={data.email}
			/>
		</div>
		<div>
			<p>Phone Number <span class="text-[#ff3561]">*</span></p>
			<input
				class="border border-1 border-[#f0f4f7] rounded-lg h-12 w-full px-2"
				type="text"
				placeholder="Enter phone number"
				bind:value={data.phone_number}
			/>
		</div>
		<div>
			<p>Referral Code (Optional)</p>
			<input
				class="border border-1 border-[#f0f4f7] rounded-lg h-12 w-full px-2"
				type="text"
				placeholder="Enter referral code"
				bind:value={data.referral_code}
			/>
		</div>
		<div>
			<p>Password <span class="text-[#ff3561]">*</span></p>
			<input
				class="border border-1 border-[#f0f4f7] rounded-lg h-12 w-full px-2"
				type="password"
				placeholder="Enter your password"
				bind:value={data.password}
			/>
		</div>
		<button
			on:click={handleSubmit}
			class="w-full rounded-md bg-[#3470e3] text-[#ffffff] border border-1 h-12">SUBMIT</button
		>
		<p class="text-center text-sm">
			By signing up, I accept the Masai <a
				class="text-[#4358F6] underline"
				href="https://masaischool.com/terms">Terms of Service</a
			>
			and acknowledge the
			<a class="text-[#4358F6] underline" href="https://masaischool.com/privacy">Privacy Policy</a>.
		</p>
	</div>
</main>
