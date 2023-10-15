<script>
	export let togglesignIn;
	function handleKeyDown(event) {
		togglesignIn();
	}

	let inputData = '';
	let inputType = ''; // This variable will store whether it's a mobile or an email

	function handleInputChange() {
		const value = inputData.trim();

		// Check if the input matches the pattern of an email
		if (/^\S+@\S+\.\S+$/.test(value)) {
			inputType = 'email';
		}
		// Check if the input matches the pattern of a phone number
		else if (/^\d{10}$/.test(value)) {
			inputType = 'mobile';
		} else {
			inputType = 'unknown';
		}
	}
</script>

<main class="flex justify-center items-center h-full">
	<div class="flex flex-col gap-5 w-full">
		<div class="text-center flex flex-col gap-3">
			<h1 class="text-3xl font-medium">Sign In</h1>
			<p class="text-lg font-medium">
				New User? <span
					on:click={togglesignIn}
					on:keydown={handleKeyDown}
					tabindex="0"
					role="button"
					class="text-[#4358F6] hover:underline hover:cursor-pointer">Sign up</span
				>
			</p>
		</div>
		<div class="flex flex-col">
			<p class="mb-1">Phone number or email address <span class="text-[#ff3561]">*</span></p>
			<input
				class="border border-1 border-[#f0f4f7] rounded-lg h-12 w-full px-2"
				type="text"
				placeholder="Enter phone number or email address"
				bind:value={inputData}
				on:input={handleInputChange}
			/>
		</div>
		<button class="w-full rounded-md bg-[#3470e3] text-[#ffffff] border border-1 h-12"
			>CONTINUE</button
		>
	</div>
</main>
