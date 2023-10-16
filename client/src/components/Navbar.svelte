<script>
	import { onMount } from 'svelte';
	import Sidebar from './Sidebar.svelte';
	import { setContext } from 'svelte';
	let isOpen = false;
	setContext('signinRoute', false);

	const toggleSidebar = () => {
		isOpen = !isOpen;
	};
	onMount(() => {
		isOpen = false;
	});
	console.log('isOpen', isOpen);
</script>

<div class="sticky top-[-1px] left-0 z-[200]">
	<div class="bg-[#FEDFE5] text-center py-[8px] relative px-[8px]">
		<p class="!font-[600] text-[16px] leading-[24px] font-sans">
			Applications for our 6th November Batches are now open!
			<button
				type="button"
				class="active:!ring-0 bg-red-500 hover:bg-red-600 rounded-[8px] text-white !font-[600] text-[12px] leading-[16px] font-sans tracking-[1.25px] uppercase p-[8px_12px] inline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 ml-[10px] mt-[6px]"
			>
				Apply now
			</button>
		</p>
	</div>

	<nav
		class=" dark:bg-gray-900 text-gray-700 dark:text-gray-200 border-gray-100 dark:border-gray-700 w-full bg-[#FFFFFF] relative z-[100] shadow-[0px_4px_6px_rgba(0,_0,_0,_0.11)] md:shadow-[0px_1px_2px_rgba(0,_0,_0,_0.06)]"
	>
		<div
			class="min-h-[64px] md:min-h-[88px] py-[12px] px-[10px] md:py-[20px] !max-w-[1280px] mx-auto flex items-center justify-between container"
		>
			<div class="flex items-center">
				<button class="lg:hidden"
					><svg
						width="24"
						height="24"
						viewBox="0 0 24 24"
						fill="none"
						xmlns="http://www.w3.org/2000/svg"
						><path d="M3 6H21V8H3V6ZM3 11H21V13H3V11ZM3 16H21V18H3V16Z" fill="#03081A" /></svg
					></button
				>
				<a href="/"
					><div
						class="max-w-[96px] max-h-[32px] md:max-w-[105px] md:max-h-[47px] flex items-center"
					>
						<img
							src="https://masai-website-images.s3.ap-south-1.amazonaws.com/logo.png"
							alt="Masai Logo"
						/>
					</div></a
				>
			</div>
			<div
				class="w-full md:block md:w-auto md:ml-[10px] lg:ml-0 hidden lg:inline-flex hover:text-[red] bg-white !p-0 border-none items-center"
				hidden="false"
			>
				<ul
					class="  space-x-[8px] md:ml-[10px] lg:ml-0 hidden lg:inline-flex hover:text-[red] bg-white !p-0 border-none items-center"
				>
					<li>
						<a
							href="/"
							class="block py-2 pr-4 pl-3 md:p-0 rounded text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
							><p
								class=" leading-[24px] tracking-[1.25px] uppercase transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 hover:!text-[#ED0331] rounded-[8px] font-[600] text-[14px] font-sans text-center hover:bg-[#FFFAFB] p-[8px] xl:p-[8px_16px] lg:text-[12px] xl:text-[14px] !text-[#03081A]"
							>
								Courses
							</p>
						</a>
					</li>
					<li>
						<a
							href="/"
							class="block py-2 pr-4 pl-3 md:p-0 rounded text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
							><p
								class="leading-[24px] tracking-[1.25px] uppercase transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 hover:!text-[#ED0331] rounded-[8px] font-[600] text-[14px] font-sans text-center hover:bg-[#FFFAFB] p-[8px] xl:p-[8px_16px] lg:text-[12px] xl:text-[14px] !text-[#03081A]"
							>
								Fees
							</p>
						</a>
					</li>
					<li>
						<a
							href="/"
							class="block py-2 pr-4 pl-3 md:p-0 rounded text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
							><p
								class="leading-[24px] tracking-[1.25px] uppercase transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 hover:!text-[#ED0331] rounded-[8px] font-[600] text-[14px] font-sans text-center hover:bg-[#FFFAFB] p-[8px] xl:p-[8px_16px] lg:text-[12px] xl:text-[14px] !text-[#03081A]"
							>
								Events
							</p>
						</a>
					</li>
					<li>
						<a
							href="/"
							class="block py-2 pr-4 pl-3 md:p-0 rounded text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
							><p
								class="leading-[24px] tracking-[1.25px] uppercase transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 hover:!text-[#ED0331] rounded-[8px] font-[600] text-[14px] font-sans text-center hover:bg-[#FFFAFB] p-[8px] xl:p-[8px_16px] lg:text-[12px] xl:text-[14px] !text-[#03081A]"
							>
								Learn
							</p>
						</a>
					</li>
					<li>
						<a
							href="/"
							class="block py-2 pr-4 pl-3 md:p-0 rounded text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
							><p
								class=" leading-[24px] tracking-[1.25px] uppercase transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 hover:!text-[#ED0331] rounded-[8px] font-[600] text-[14px] font-sans text-center hover:bg-[#FFFAFB] p-[8px] xl:p-[8px_16px] lg:text-[12px] xl:text-[14px] !text-[#03081A]"
							>
								Success Stories
							</p>
						</a>
					</li>
					<li>
						<a
							href="/"
							class="block py-2 pr-4 pl-3 md:p-0 rounded text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
							><p
								class="leading-[24px] tracking-[1.25px] uppercase transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 hover:!text-[#ED0331] rounded-[8px] font-[600] text-[14px] font-sans text-center hover:bg-[#FFFAFB] p-[8px] xl:p-[8px_16px] lg:text-[12px] xl:text-[14px] !text-[#03081A]"
							>
								Hire From Us
							</p>
						</a>
					</li>
				</ul>
			</div>
			<div class="flex items-center gap-[8px] xl:gap-[16px]">
				<div class="overflow-hidden relative flex items-center">
					<div class="absolute">
						<div class="w-full h-full pointer-events-none" />
					</div>
				</div>
				<a
					href="/"
					disabled="false"
					class="active:!ring-0 rounded-[8px] text-white !font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase p-[12px_16px] focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 w-fit md:px-[8px] hidden md:flex !bg-[#E5FEFF] hover:!bg-[#CFE9EE] whitespace-nowrap"
					style="color: rgb(110, 113, 204) !important;">Refer &amp; Earn</a
				>
				<a
					href="/"
					disabled="false"
					class="active:!ring-0 rounded-[8px] text-white leading-[24px] font-sans tracking-[1.25px] uppercase p-[8px_12px] focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 px-[8px] md:hidden !bg-[#E5FEFF] hover:!bg-[#CFE9EE] text-[12px] !font-[600] flex whitespace-nowrap"
					style="color: rgb(110, 113, 204) !important;">Refer &amp; Earn</a
				>
				<button
					type="button"
					class="bg-transparent border border-red-500 !text-primary-red-500 hover:bg-red-100 focus-visible:bg-white rounded-[8px] !font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase p-[12px_16px] focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 hidden md:block"
					on:click={() => (isOpen = true)}>sign up</button
				>
				<button
					type="button"
					class="bg-transparent !text-primary-red-500 hover:bg-red-100 focus-visible:!bg-white rounded-[8px] !font-[600] text-[12px] leading-[16px] font-sans tracking-[1.25px] uppercase p-[8px_12px] focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 block md:hidden"
					>sign up</button
				>
			</div>
		</div>
	</nav>
	{#if isOpen}
		<Sidebar bind:isOpen on:close={() => (isOpen = false)} />
	{/if}
</div>

<!-- <div
	class="sticky top-[var(--top)] md:top-[var(--top)] left-0 z-[160]"
	style="box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 3px, rgba(0, 0, 0, 0.06) 0px 1px 2px; --top: 136px;"
>
	<div
		class="absolute grid closed lg:hidden w-screen bg-white border-none svelte-159q009"
		style="--endingHeight: 100vh; --startingHeight: 0vh; transition: max-height 0.3s ease-out 0s, grid-template-rows 0.3s ease-out 0s;"
	>
		<div class="grid left-0 right-0 overflow-hidden undefined svelte-159q009">
			<ul class="mt-0 pt-[8px]">
				<a href="/" class="hover:!bg-white"
					><p
						class="!font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !text-[#03081A] hover:!text-[#ED0331] hover:bg-[#FFFAFB] text-[16px] px-4 py-2"
					>
						Courses
					</p>
				</a><a href="/" class="hover:!bg-white"
					><p
						class="!font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !text-[#03081A] hover:!text-[#ED0331] hover:bg-[#FFFAFB] text-[16px] px-4 py-2"
					>
						Fees
					</p>
				</a><a href="/" class="hover:!bg-white"
					><p
						class="!font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !text-[#03081A] hover:!text-[#ED0331] hover:bg-[#FFFAFB] text-[16px] px-4 py-2"
					>
						Events
					</p>
				</a><a href="/" class="hover:!bg-white"
					><p
						class="!font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !text-[#03081A] hover:!text-[#ED0331] hover:bg-[#FFFAFB] text-[16px] px-4 py-2"
					>
						Learn
					</p>
				</a><a href="/" class="hover:!bg-white"
					><p
						class="!font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !text-[#03081A] hover:!text-[#ED0331] hover:bg-[#FFFAFB] text-[16px] px-4 py-2"
					>
						Success Stories
					</p>
				</a><a href="/" class="hover:!bg-white"
					><p
						class="!font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !text-[#03081A] hover:!text-[#ED0331] hover:bg-[#FFFAFB] text-[16px] px-4 py-2"
					>
						Hire From Us
					</p>
				</a>
			</ul>
		</div>
	</div>
</div> -->

<style>
</style>
