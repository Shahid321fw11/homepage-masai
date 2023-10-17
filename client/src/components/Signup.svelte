<script>
	import { toast } from '@zerodevx/svelte-toast';
	export let togglesignIn;
	import OtpInput from '@k4ung/svelte-otp';

	let data = {
		full_name: '',
		email: '',
		phone_number: '',
		referral_code: '',
		password: ''
	};
	let isLoading = false;
	let isValidation = false;
	let otp = '';
	function handleKeyDown(event) {
		if (event.keyCode == 'Enter') {
			return handleForm();
		}
	}
	async function handleForm() {
		const requestData = JSON.stringify(data);

		const url = '';
		if (!data.full_name) {
			toast.push('Please enter a full name', {
				theme: {
					'--toastColor': 'mintcream',
					'--toastBackground': 'red',
					'--toastBarBackground': 'red'
				}
			});
			return;
		}
		if (!isValidEmail(data.email)) {
			toast.push('Please enter a valid email address.', {
				theme: {
					'--toastColor': 'mintcream',
					'--toastBackground': 'rgba(72,187,120,0.9)',
					'--toastBarBackground': '#2F855A'
				}
			});
			return;
		}
		if (!isValidPhoneNumber(data.phone_number)) {
			toast.push('Please enter a valid phone number', {
				theme: {
					'--toastColor': 'mintcream',
					'--toastBackground': 'red',
					'--toastBarBackground': 'red'
				}
			});
			return;
		}
		isLoading = true;
		const response = await fetch('https://raj74434.pythonanywhere.com/signUp', {
			method: 'POST',
			body: JSON.stringify(data),
			headers: {
				'Content-Type': 'application/json'
			}
		});
		const res = await response.json();
		console.log(res);

		toast.push(`User with email ${data.email} registered Succesfuly `, {
			theme: {
				'--toastColor': 'mintcream',
				'--toastBackground': '#50C878',
				'--toastBarBackground': 'green'
			}
		});
		isLoading = false;
		togglesignIn();
	}
	async function handleValidation() {
		isValidation = false;
	}
	$: {
		console.log('this is otp', otp);
		console.log('this is data', data);
	}

	function isValidEmail(email) {
		return email.includes('@') && email.includes('.');
	}

	// Helper function to validate phone number
	function isValidPhoneNumber(phoneNumber) {
		return /\d{10}/.test(phoneNumber);
	}
</script>

<main class=" flex flex-col gap-3">
	<div class={isValidation ? 'text-left' : 'text-center'}>
		<h1
			class="font-[650] text-[24px] leading-[32px] font-poppins transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 text-center text-[#03081A]"
		>
			{#if isValidation} Verify Email {:else} Create Account {/if}
		</h1>
		<p
			class="!font-[500] text-[16px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 text-center mt-4 flex gap-[8px] justify-center flex-wrap"
		>
			{#if isValidation}
				Enter OTP sent to {data.email}
			{:else}
				Already have an account? <span
					class="!font-[600] text-[16px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 text-[#4358F6]"
					on:click={togglesignIn}
					on:keydown={handleKeyDown}
					tabindex="0"
					role="button">Sign In</span
				>
			{/if}
		</p>
	</div>

	<div class="flex flex-col gap-4">
		{#if isValidation}
			<div class="flex justify-center items-start">
				<OtpInput
					bind:value={otp}
					inputClass="default-input w-[45px] md:w-[50px] h-[45px] md:h-[50px] bg-[#F3F3F3] text-[#515151] rounded-[8px] !font-[600] text-[24px] leading-[34px] font-sans svelte-1qbn7j"
					numOfInputs={6}
				/>
			</div>
		{:else}
			<div>
				<p
					class="!font-[450] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !text-[#21191B]"
				>
					Full Name <span class="text-[#ff3561]">*</span>
				</p>
				<input
					class="input-transition focus-visible:border-[#3182ce] focus-visible:shadow-[rgb(49_130_206)_0px_0px_0px_1px] w-[100%] rounded-[8px] p-[12px] !outline-none placeholder-ms-grey-400 border-[1px] border-solid relative border-[#E2E8F0] svelte-my2qxg"
					type="text"
					placeholder="Enter your Full name"
					bind:value={data.full_name}
				/>
			</div>
			<div>
				<p
					class="!font-[450] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !text-[#21191B]"
				>
					Email address <span class="text-[#ff3561]">*</span>
				</p>
				<input
					class="input-transition focus-visible:border-[#3182ce] focus-visible:shadow-[rgb(49_130_206)_0px_0px_0px_1px] w-[100%] rounded-[8px] p-[12px] !outline-none placeholder-ms-grey-400 border-[1px] border-solid relative border-[#E2E8F0] svelte-my2qxg"
					type="text"
					placeholder="Enter email address"
					bind:value={data.email}
				/>
			</div>
			<div>
				<p
					class="!font-[450] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !text-[#21191B]"
				>
					Phone Number <span class="text-[#ff3561]">*</span>
				</p>
				<input
					class="input-transition focus-visible:border-[#3182ce] focus-visible:shadow-[rgb(49_130_206)_0px_0px_0px_1px] w-[100%] rounded-[8px] p-[12px] !outline-none placeholder-ms-grey-400 border-[1px] border-solid relative border-[#E2E8F0] svelte-my2qxg"
					type="text"
					placeholder="Enter phone number"
					bind:value={data.phone_number}
				/>
			</div>
			<div>
				<p
					class="!font-[450] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !text-[#21191B]"
				>
					Password <span class="text-[#ff3561]">*</span>
				</p>
				<input
					class="input-transition focus-visible:border-[#3182ce] focus-visible:shadow-[rgb(49_130_206)_0px_0px_0px_1px] w-[100%] rounded-[8px] p-[12px] !outline-none placeholder-ms-grey-400 border-[1px] border-solid relative border-[#E2E8F0] svelte-my2qxg"
					type="text"
					placeholder="Enter referral code"
					bind:value={data.password}
				/>
			</div>
			<div>
				<p
					class="!font-[450] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !text-[#21191B]"
				>
					Referral Code (Optional)
				</p>
				<input
					class="input-transition focus-visible:border-[#3182ce] focus-visible:shadow-[rgb(49_130_206)_0px_0px_0px_1px] w-[100%] rounded-[8px] p-[12px] !outline-none placeholder-ms-grey-400 border-[1px] border-solid relative border-[#E2E8F0] svelte-my2qxg"
					type="text"
					placeholder="Enter referral code"
					bind:value={data.referral_code}
				/>
			</div>
		{/if}
		<!-- <SignupForm bind:data {handleSubmit} {togglesignIn} /> -->
		<button
			on:click={isValidation ? handleValidation : handleForm}
			class="active:!ring-0 !bg-[#3470E4] hover:!bg-[#1647A5] rounded-[8px] text-[#FFFFFF] !font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase p-[12px_16px] inline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 w-full"
			style="display: flex; justify-content: center; align-items: center;"
		>
			{#if !isValidation && !isLoading}
				SUBMIT
			{:else if !isValidation && isLoading}
				<div class="w-full flex justify-center items-center">
					<svg
						aria-hidden="true"
						class="inline w-4 h-4 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
						viewBox="0 0 100 101"
						fill="none"
						xmlns="http://www.w3.org/2000/svg"
						style="height: 100%;"
					>
						<path
							d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
							fill="currentColor"
						/>
						<path
							d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
							fill="currentFill"
						/>
					</svg>
				</div>
			{:else if isValidation && !isLoading}
				VERIFY
			{:else}
				<div class="flex justify-normal items-center">
					<svg
						aria-hidden="true"
						class="inline w-4 h-4 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
						viewBox="0 0 100 101"
						fill="none"
						xmlns="http://www.w3.org/2000/svg"
						style="height: 100%;"
					>
						<path
							d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
							fill="currentColor"
						/>
						<path
							d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
							fill="currentFill"
						/>
					</svg>
				</div>
			{/if}
		</button>

		{#if !isValidation}
			<p
				class="!font-[400] text-[12px] leading-[16px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 text-center py-[8px]"
			>
				By signing up, I accept the Masai <a
					class="text-[#4358F6] underline"
					href="https://masaischool.com/terms">Terms of Service</a
				>
				and acknowledge the
				<a class="text-[#4358F6] underline" href="https://masaischool.com/privacy">Privacy Policy</a
				>.
			</p>
		{/if}
	</div>
</main>
