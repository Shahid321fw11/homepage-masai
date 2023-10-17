<script>
	export let togglesignIn;
	import { toast } from '@zerodevx/svelte-toast';
	function handleKeyDown(event) {
		togglesignIn();
	}

	let inputData = { identifier: '', password: '' };
	let isLoading = false;
	async function handleSubmit() {
		isLoading = true;
		try {
			const res = await fetch('https://raj74434.pythonanywhere.com/signIn', {
				method: 'POST',
				body: JSON.stringify(inputData),
				headers: {
					'Content-Type': 'application/json'
				}
			});
			const response = await res.json();
			if (response) {
				toast.push('logged in successfully', {
					theme: {
						'--toastColor': 'mintcream',
						'--toastBackground': '#50C878',
						'--toastBarBackground': 'green'
					}
				});
				isLoading = false;
			}
		} catch (error) {
			console.error(error);
			isLoading = false;
		}
	}
</script>

<main class="flex justify-center items-center h-full">
	<div class="flex flex-col gap-5 w-full">
		<div class="text-center flex flex-col gap-3">
			<h1
				class="font-[650] text-[24px] leading-[32px] font-poppins transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 text-center text-[#03081A"
			>
				Sign In
			</h1>
			<p
				class="!font-[500] text-[16px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 text-center mt-4 flex gap-[8px] justify-center flex-wrap"
			>
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
			<p
				class="!font-[450] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !text-[#21191B]"
			>
				Phone number or email address <span class="text-[#ff3561]">*</span>
			</p>
			<input
				class="input-transition focus-visible:border-[#3182ce] focus-visible:shadow-[rgb(49_130_206)_0px_0px_0px_1px] w-[100%] rounded-[8px] p-[12px] !outline-none placeholder-ms-grey-400 border-[1px] border-solid relative border-[#E2E8F0] svelte-my2qxg"
				type="text"
				placeholder="Enter phone number or email address"
				bind:value={inputData.identifier}
			/>
		</div>
		<div class="flex flex-col">
			<p
				class="!font-[450] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !text-[#21191B]"
			>
				Enter your password <span class="text-[#ff3561]">*</span>
			</p>
			<input
				class="input-transition focus-visible:border-[#3182ce] focus-visible:shadow-[rgb(49_130_206)_0px_0px_0px_1px] w-[100%] rounded-[8px] p-[12px] !outline-none placeholder-ms-grey-400 border-[1px] border-solid relative border-[#E2E8F0] svelte-my2qxg"
				type="password"
				placeholder="Enter your password"
				bind:value={inputData.password}
			/>
		</div>

		<button
			class="active:!ring-0 !bg-[#3470E4] hover:!bg-[#1647A5] rounded-[8px] text-[#FFFFFF] !font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase p-[12px_16px] inline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 w-full"
			on:click={handleSubmit}
			>{#if isLoading}
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
			{:else}
				SUBMIT
			{/if}</button
		>
	</div>
</main>
