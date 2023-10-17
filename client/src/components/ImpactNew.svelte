<script>
	import Carousel from 'svelte-carousel';

	const childEle = [
		`<div
								class="swiper-slide w-full !h-auto overflow-hidden svelte-jnbt72 swiper-slide-active"
								style="width: 608px;"
								data-swiper-slide-index="0"
							>
								<div class="h-full" slot="swiper-slide-content">
									<div class="rounded-[15px] h-full max-h-fit m-auto bg-transparent">
										<div
											class="max-h-fit overflow-hidden bg-transparent rounded-[16px] border border-[#CECCCD]"
										>
											<div class="bg-transparent false">
												<div style="padding-top: 56.25%" class="svelte-a8ul8k fluidWrapper">
													<div>
														<div
															class="react-player"
															style="border-radius: 16px; overflow: hidden; width: 100%; height: 100%;"
														>
															<div
																style="width: 100%; height: 100%; overflow: hidden;"
																data-vimeo-initialized="true"
															>
																<iframe
																	src="https://player.vimeo.com/video/867869719?title=0&amp;byline=0&amp;portrait=0&amp;playsinline=0&amp;autopause=0&amp;app_id=122963"
																	width="426"
																	height="240"
																	frameborder="0"
																	allow="autoplay; fullscreen; picture-in-picture"
																	title="Masai Is Building A Great Solution - Ankush Sachdeva, CEO - ShareChat"
																	data-ready="true"
																	style="width: 100%; height: 100%;"
																/>
															</div>
														</div>
													</div>
												</div>
											</div>
										</div>
									</div>
								</div>
							</div>`,
		`							<div
								class="swiper-slide w-full !h-auto overflow-hidden svelte-jnbt72 swiper-slide-next"
								style="width: 608px;"
								data-swiper-slide-index="1"
							>
								<div class="h-full" slot="swiper-slide-content">
									<div class="rounded-[15px] h-full max-h-fit m-auto bg-transparent">
										<div
											class="max-h-fit overflow-hidden bg-transparent rounded-[16px] border border-[#CECCCD]"
										>
											<div class="bg-transparent false">
												<div style="padding-top: 56.25%" class="svelte-a8ul8k fluidWrapper">
													<div>
														<div
															class="react-player"
															style="border-radius: 16px; overflow: hidden; width: 100%; height: 100%;"
														>
															<div
																style="width: 100%; height: 100%; overflow: hidden;"
																data-vimeo-initialized="true"
															>
																<iframe
																	src="https://player.vimeo.com/video/868222145?title=0&amp;byline=0&amp;portrait=0&amp;playsinline=0&amp;autopause=0&amp;app_id=122963"
																	width="426"
																	height="240"
																	frameborder="0"
																	allow="autoplay; fullscreen; picture-in-picture"
																	title="Masai Partners Speak- @NoBrokerOfficial Highly Recommends Hiring Masai Graduates �"
																	data-ready="true"
																	style="width: 100%; height: 100%;"
																/>
															</div>
														</div>
													</div>
												</div>
											</div>
										</div>
									</div>
								</div>
							</div>`,
		`<div
								class="swiper-slide w-full !h-auto overflow-hidden svelte-jnbt72"
								data-swiper-slide-index="2"
								style="width: 608px;"
							>
								<div class="h-full" slot="swiper-slide-content">
									<div class="rounded-[15px] h-full max-h-fit m-auto bg-transparent">
										<div
											class="max-h-fit overflow-hidden bg-transparent rounded-[16px] border border-[#CECCCD]"
										>
											<div class="bg-transparent false">
												<div style="padding-top: 56.25%" class="svelte-a8ul8k fluidWrapper">
													<div>
														<div
															class="react-player"
															style="border-radius: 16px; overflow: hidden; width: 100%; height: 100%;"
														>
															<div
																style="width: 100%; height: 100%; overflow: hidden;"
																data-vimeo-initialized="true"
															>
																<iframe
																	src="https://player.vimeo.com/video/868221344?title=0&amp;byline=0&amp;portrait=0&amp;playsinline=0&amp;autopause=0&amp;app_id=122963"
																	width="426"
																	height="240"
																	frameborder="0"
																	allow="autoplay; fullscreen; picture-in-picture"
																	title="Masai Being A Solution To Tech Hiring  Masai Partners Speak"
																	data-ready="true"
																	style="width: 100%; height: 100%;"
																/>
															</div>
														</div>
													</div>
												</div>
											</div>
										</div>
									</div>
								</div>
							</div>
`
	];

	// const images = [
	// 	{
	// 		url: 'https://res.cloudinary.com/beswift/image/upload/v1650391490/photo-1644241687200-eadaf7601290_xcz2kh.jpg',
	// 		description: 'image1'
	// 	},
	// 	{
	// 		url: 'https://res.cloudinary.com/beswift/image/upload/v1650391337/photo-1647067867267-e01d98462f3c_ugtnwe.jpg',
	// 		description: 'image2'
	// 	},
	// 	{
	// 		url: 'https://res.cloudinary.com/beswift/image/upload/v1650391131/photo-1648800475313-2bb7fbec8701_ae60yw.jpg',
	// 		description: 'image3'
	// 	},
	// 	{
	// 		url: 'https://res.cloudinary.com/beswift/image/upload/v1650390102/photo-1649894222226-056a1a79d9fb_xlv73h.jpg',
	// 		description: 'image4'
	// 	},
	// 	{
	// 		url: 'https://res.cloudinary.com/beswift/image/upload/v1650389425/photo-1649894221695-45abb718a190_sgjhwd.jpg',
	// 		description: 'image5'
	// 	}
	// ];
	let carousel; // for calling methods of the carousel instance
	const handleNextClick = () => {
		carousel.goToNext();
	};
</script>

<div class="md:px-[16px] bg-[#F9F9F9]">
	<div class="py-[32px] md:py-[50px] undefined">
		<h2
			class="font-[700] text-[34px] leading-[40px] font-poppins transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 text-center mb-[24px] max-w-[1280px] mx-auto"
		>
			Our Students Are
			<span class="!text-[#ED0331] relative whitespace-nowrap isolate"
				>Creating Impact
				<img
					loading="lazy"
					alt="yellow-vector"
					class="mx-auto absolute w-full md:w-[264px] bottom-[-8px] md:bottom-[-10px] z-[-1] h-[14px] md:h-[21px] left-0 right-0"
					style="opacity: 1; transition: opacity 1200ms ease-out 0s;"
					src="https://masaischool.com/images/new-homepage/yellow-vector.svg"
				/></span
			>
		</h2>
		<div
			class="mt-[37px] md:mt-[72px] max-w-[1280px] mx-auto grid grid-cols-1 lg:grid-cols-[49%_49%] xl:grid-cols-[50%_50%] gap-[20px] undefined"
		>
			<!--  -->
			<!-- <Carousel
				bind:this={carousel}
				let:loaded
				autoplay
				autoplayDuration={3000}
				autoplayProgressVisible
			>
				{#each images as src, imageIndex (src)}
					<div class="img-container">
						{#if loaded.includes(imageIndex)}
							<img src={src.url} alt={src.description} width={1000} height={600} />
						{/if}
					</div>
				{/each}
			</Carousel> -->
			<!--  -->

			<div class="mt-[-20px] mb-[-32px] h-fit relative">
				<div class="mb-[32px] mt-[20px] w-[100%] false !px-[16px] svelte-jnbt72">
					<div
						class="company-testimonials swiper svelte-jnbt72 swiper-initialized swiper-horizontal swiper-backface-hidden"
					>
						<div
							class="swiper-wrapper false flex svelte-jnbt72"
							style="transform: translate3d(0px, 0px, 0px);"
						>
							<Carousel ind:this={carousel}>
								{#each childEle as ele}
									{ele}
								{/each}
							</Carousel>
						</div>
					</div>
				</div>
				<div
					class="mx-auto w-full top-0 h-full items-center company-testimonials-pagination absolute z-[1] flex justify-between pointer-events-none"
				>
					<button
						type="button"
						class="active:!ring-0 bg-ms-red-500 hover:bg-ms-red-600 rounded-[8px] text-white !font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase p-[12px_16px] inline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !bg-[white] hover:!bg-gray-200 active:!bg-gray-300 !text-[#0A0103] h-[40px] w-[40px] !p-0 company-testimonials-prev pointer-events-auto flex justify-center items-center !rounded-[50%]"
						style="box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px !important;"
						><div>
							<svg
								width="24"
								height="24"
								fill="currentColor"
								viewBox="0 0 24 24"
								class=""
								xmlns="http://www.w3.org/2000/svg"
								><path
									d="M15.41 16.58L10.83 12L15.41 7.41L14 6L7.99997 12L14 18L15.41 16.58Z"
									fill="currentColor"
								/></svg
							>
						</div></button
					>
					<button
						type="button"
						class="active:!ring-0 bg-ms-red-500 hover:bg-ms-red-600 rounded-[8px] text-white !font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase p-[12px_16px] inline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !bg-[white] hover:!bg-gray-200 active:!bg-gray-300 !text-[#0A0103] h-[40px] w-[40px] !p-0 company-testimonials-next pointer-events-auto flex justify-center items-center !rounded-[50%]"
						style="box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px !important;"
						><div>
							<svg
								width="24"
								height="24"
								fill="currentColor"
								viewBox="0 0 24 24"
								class=""
								xmlns="http://www.w3.org/2000/svg"
								><path
									d="M8.59003 16.58L13.17 12L8.59003 7.41L10 6L16 12L10 18L8.59003 16.58Z"
									fill="currentColor"
								/></svg
							>
						</div></button
					>
				</div>
			</div>
			<!-- <div>
				<div>
					<div class="mb-[32px] mt-[20px] w-[100%] false !m-0 svelte-jnbt72">
						<div
							class="company-review-card swiper !px-[16px] md:!px-0 !pb-[20px] svelte-jnbt72 swiper-initialized swiper-horizontal swiper-backface-hidden"
						>
							<div
								class="swiper-wrapper false svelte-jnbt72"
								style="transform: translate3d(0px, 0px, 0px);"
							>
								<div
									class="swiper-slide w-full !h-auto svelte-jnbt72 swiper-slide-active"
									style="width: 361.429px; margin-right: 10px;"
								>
									<div class="h-full" slot="swiper-slide-content">
										<button
											style="background:#fff;border:1px solid #CFD0EE;box-shadow:0px 1px 3px rgba(0, 0, 0, 0.1), 0px 1px 2px rgba(0, 0, 0, 0.06);"
											class="relative isolate h-full rounded-[24px] cursor-default text-left p-[24px] pb-[24px] md:pb-[12px] lg:max-w-[350px]"
										>
											<a
												href="https://www.linkedin.com/in/aryaag/"
												class="w-fit block ml-auto"
												target="_blank"
												><img
													alt="linkedin"
													class="ml-auto"
													style="opacity: 1; transition: opacity 1200ms ease-out 0s;"
													src="https://masaischool.com/images/linkedin.svg"
												/></a
											>
											<div class="flex mt-[16px] text-ms-gray-700">
												<div>
													<svg viewBox="0 0 12 10" class="w-[12px] h-[10px]" style="color:undefined"
														><path
															fill="currentColor"
															d="M0.519531 9.20006V6.36006C0.519531 5.26676 0.692861 4.25336 1.03953 3.32006C1.41286 2.38673 2.03953 1.46673 2.91953 0.560059L4.47953 1.72006C3.89286 2.36006 3.4662 2.96006 3.19953 3.52006C2.93286 4.05336 2.77286 4.58676 2.71953 5.12006H4.59953V9.20006H0.519531ZM7.15953 9.20006V6.36006C7.15953 5.26676 7.33283 4.25336 7.67953 3.32006C8.05283 2.38673 8.67953 1.46673 9.55953 0.560059L11.1195 1.72006C10.5328 2.36006 10.1062 2.96006 9.83953 3.52006C9.57283 4.05336 9.41283 4.58676 9.35953 5.12006H11.2395V9.20006H7.15953Z"
														/></svg
													>
												</div>
												<p
													class="!font-[400] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 ml-[8px]"
												>
													Masai does a great job of attracting ambitious folk and it shows in the
													hunger with which the grads ...
												</p>
											</div>
											<div class="flex items-center mt-[16px]" />
											<div class="flex items-center mt-[16px]">
												<img
													class="rounded-[8px] w-[48px] h-[48px] mr-[8px]"
													style="opacity: 1; transition: opacity 1200ms ease-out 0s;"
													src="https://masai-website-images.s3.ap-south-1.amazonaws.com/Arya_Adarsha_Gautam_a72b51d7b3.jpeg"
												/>
												<div>
													<p
														class="!font-[600] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 mb-[4px]"
													>
														Arya Adarsha Gautam
													</p>
													<div class="flex">
														<p
															class="!font-[400] text-[12px] leading-[16px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 undefined"
														>
															CTO and Co-Founder -
														</p>
														<p
															class="!font-[400] text-[12px] leading-[16px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 ml-[4px]"
														>
															Pagarbook
														</p>
													</div>
												</div>
											</div>
											<img
												class="mt-[16px] ml-[-8px] w-[93px]"
												alt="company logo"
												style=""
												src="https://masai-website-images.s3.ap-south-1.amazonaws.com/pagarbook_rect_adcdc345e4.svg"
											/></button
										>
									</div>
								</div>
								<div
									class="swiper-slide w-full !h-auto svelte-jnbt72 swiper-slide-next"
									style="width: 361.429px; margin-right: 10px;"
								>
									<div class="h-full" slot="swiper-slide-content">
										<button
											style="background:#fff;border:1px solid #CFD0EE;box-shadow:0px 1px 3px rgba(0, 0, 0, 0.1), 0px 1px 2px rgba(0, 0, 0, 0.06);"
											class="relative isolate h-full rounded-[24px] cursor-default text-left p-[24px] pb-[24px] md:pb-[12px] lg:max-w-[350px]"
										>
											<a
												href="https://www.linkedin.com/in/anirvan--majumdar/"
												class="w-fit block ml-auto"
												target="_blank"
												><img
													alt="linkedin"
													class="ml-auto"
													style="opacity: 1; transition: opacity 1200ms ease-out 0s;"
													src="https://masaischool.com/images/linkedin.svg"
												/></a
											>
											<div class="flex mt-[16px] text-ms-gray-700">
												<div>
													<svg viewBox="0 0 12 10" class="w-[12px] h-[10px]" style="color:undefined"
														><path
															fill="currentColor"
															d="M0.519531 9.20006V6.36006C0.519531 5.26676 0.692861 4.25336 1.03953 3.32006C1.41286 2.38673 2.03953 1.46673 2.91953 0.560059L4.47953 1.72006C3.89286 2.36006 3.4662 2.96006 3.19953 3.52006C2.93286 4.05336 2.77286 4.58676 2.71953 5.12006H4.59953V9.20006H0.519531ZM7.15953 9.20006V6.36006C7.15953 5.26676 7.33283 4.25336 7.67953 3.32006C8.05283 2.38673 8.67953 1.46673 9.55953 0.560059L11.1195 1.72006C10.5328 2.36006 10.1062 2.96006 9.83953 3.52006C9.57283 4.05336 9.41283 4.58676 9.35953 5.12006H11.2395V9.20006H7.15953Z"
														/></svg
													>
												</div>
												<p
													class="!font-[400] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 ml-[8px]"
												>
													There are many platforms that bolster an individual's "knowledge" to show
													up to work and just do the...
												</p>
											</div>
											<div class="flex items-center mt-[16px]" />
											<div class="flex items-center mt-[16px]">
												<img
													class="rounded-[8px] w-[48px] h-[48px] mr-[8px]"
													style="opacity: 1; transition: opacity 1200ms ease-out 0s;"
													src="https://masai-website-images.s3.ap-south-1.amazonaws.com/Anirban_Majumdar_e001629fcc.jpeg"
												/>
												<div>
													<p
														class="!font-[600] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 mb-[4px]"
													>
														Anirban Majumdar
													</p>
													<div class="flex">
														<p
															class="!font-[400] text-[12px] leading-[16px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 undefined"
														>
															CTO and Co-Founder -
														</p>
														<p
															class="!font-[400] text-[12px] leading-[16px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 ml-[4px]"
														>
															Urban Piper
														</p>
													</div>
												</div>
											</div>
											<img
												class="mt-[16px] ml-[-8px] w-[93px]"
												alt="company logo"
												style=""
												src="https://masai-website-images.s3.ap-south-1.amazonaws.com/urbanpiper_rect_37c839e35e.svg"
											/></button
										>
									</div>
								</div>
								<div
									class="swiper-slide w-full !h-auto svelte-jnbt72"
									style="width: 361.429px; margin-right: 10px;"
								>
									<div class="h-full" slot="swiper-slide-content">
										<button
											style="background:#fff;border:1px solid #CFD0EE;box-shadow:0px 1px 3px rgba(0, 0, 0, 0.1), 0px 1px 2px rgba(0, 0, 0, 0.06);"
											class="relative isolate h-full rounded-[24px] cursor-default text-left p-[24px] pb-[24px] md:pb-[12px] lg:max-w-[350px]"
										>
											<a
												href="https://www.linkedin.com/in/vamsee-mohan-kamabathula/"
												class="w-fit block ml-auto"
												target="_blank"
												><img
													alt="linkedin"
													class="ml-auto min-h-[24px]"
													style="opacity: 0; transition: opacity 1200ms ease-out 0s;"
												/></a
											>
											<div class="flex mt-[16px] text-ms-gray-700">
												<div>
													<svg viewBox="0 0 12 10" class="w-[12px] h-[10px]" style="color:undefined"
														><path
															fill="currentColor"
															d="M0.519531 9.20006V6.36006C0.519531 5.26676 0.692861 4.25336 1.03953 3.32006C1.41286 2.38673 2.03953 1.46673 2.91953 0.560059L4.47953 1.72006C3.89286 2.36006 3.4662 2.96006 3.19953 3.52006C2.93286 4.05336 2.77286 4.58676 2.71953 5.12006H4.59953V9.20006H0.519531ZM7.15953 9.20006V6.36006C7.15953 5.26676 7.33283 4.25336 7.67953 3.32006C8.05283 2.38673 8.67953 1.46673 9.55953 0.560059L11.1195 1.72006C10.5328 2.36006 10.1062 2.96006 9.83953 3.52006C9.57283 4.05336 9.41283 4.58676 9.35953 5.12006H11.2395V9.20006H7.15953Z"
														/></svg
													>
												</div>
												<p
													class="!font-[400] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 ml-[8px]"
												>
													We were looking to hire entry-level developers and Masai more than
													delivered. Our selection rate fro...
												</p>
											</div>
											<div class="flex items-center mt-[16px]" />
											<div class="flex items-center mt-[16px]">
												<img
													class="rounded-[8px] w-[48px] h-[48px] mr-[8px] min-h-[48px]"
													style="opacity: 0; transition: opacity 1200ms ease-out 0s;"
												/>
												<div>
													<p
														class="!font-[600] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 mb-[4px]"
													>
														Vamsee Mohan Kamabathula
													</p>
													<div class="flex">
														<p
															class="!font-[400] text-[12px] leading-[16px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 undefined"
														>
															CTO and Co-Founder -
														</p>
														<p
															class="!font-[400] text-[12px] leading-[16px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 ml-[4px]"
														>
															Qapita Fintech
														</p>
													</div>
												</div>
											</div>
											<img
												class="mt-[16px] ml-[-8px] w-[93px] min-h-[31.88px]"
												alt="company logo"
												style="height: 31.88px;"
											/></button
										>
									</div>
								</div>
								<div
									class="swiper-slide w-full !h-auto svelte-jnbt72"
									style="width: 361.429px; margin-right: 10px;"
								>
									<div class="h-full" slot="swiper-slide-content">
										<button
											style="background:#fff;border:1px solid #CFD0EE;box-shadow:0px 1px 3px rgba(0, 0, 0, 0.1), 0px 1px 2px rgba(0, 0, 0, 0.06);"
											class="relative isolate h-full rounded-[24px] cursor-default text-left p-[24px] pb-[24px] md:pb-[12px] lg:max-w-[350px]"
										>
											<a
												href="https://www.linkedin.com/in/pradeep-sreeram/"
												class="w-fit block ml-auto"
												target="_blank"
												><img
													alt="linkedin"
													class="ml-auto min-h-[24px]"
													style="opacity: 0; transition: opacity 1200ms ease-out 0s;"
												/></a
											>
											<div class="flex mt-[16px] text-ms-gray-700">
												<div>
													<svg viewBox="0 0 12 10" class="w-[12px] h-[10px]" style="color:undefined"
														><path
															fill="currentColor"
															d="M0.519531 9.20006V6.36006C0.519531 5.26676 0.692861 4.25336 1.03953 3.32006C1.41286 2.38673 2.03953 1.46673 2.91953 0.560059L4.47953 1.72006C3.89286 2.36006 3.4662 2.96006 3.19953 3.52006C2.93286 4.05336 2.77286 4.58676 2.71953 5.12006H4.59953V9.20006H0.519531ZM7.15953 9.20006V6.36006C7.15953 5.26676 7.33283 4.25336 7.67953 3.32006C8.05283 2.38673 8.67953 1.46673 9.55953 0.560059L11.1195 1.72006C10.5328 2.36006 10.1062 2.96006 9.83953 3.52006C9.57283 4.05336 9.41283 4.58676 9.35953 5.12006H11.2395V9.20006H7.15953Z"
														/></svg
													>
												</div>
												<p
													class="!font-[400] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 ml-[8px]"
												>
													Hiring experience with Masai is a wow. All the candidates we interviewed
													were equally talented, sele...
												</p>
											</div>
											<div class="flex items-center mt-[16px]" />
											<div class="flex items-center mt-[16px]">
												<img
													class="rounded-[8px] w-[48px] h-[48px] mr-[8px] min-h-[48px]"
													style="opacity: 0; transition: opacity 1200ms ease-out 0s;"
												/>
												<div>
													<p
														class="!font-[600] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 mb-[4px]"
													>
														Pradeep Sreeram
													</p>
													<div class="flex">
														<p
															class="!font-[400] text-[12px] leading-[16px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 undefined"
														>
															Engineering Lead -
														</p>
														<p
															class="!font-[400] text-[12px] leading-[16px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 ml-[4px]"
														>
															Eat.Fit
														</p>
													</div>
												</div>
											</div>
											<img
												class="mt-[16px] ml-[-8px] w-[93px] min-h-[31.88px]"
												alt="company logo"
												style="height: 31.88px;"
											/></button
										>
									</div>
								</div>
								<div
									class="swiper-slide w-full !h-auto svelte-jnbt72"
									style="width: 361.429px; margin-right: 10px;"
								>
									<div class="h-full" slot="swiper-slide-content">
										<button
											style="background:#fff;border:1px solid #CFD0EE;box-shadow:0px 1px 3px rgba(0, 0, 0, 0.1), 0px 1px 2px rgba(0, 0, 0, 0.06);"
											class="relative isolate h-full rounded-[24px] cursor-default text-left p-[24px] pb-[24px] md:pb-[12px] lg:max-w-[350px]"
										>
											<a
												href="https://www.linkedin.com/in/arshdeep-singh-makker"
												class="w-fit block ml-auto"
												target="_blank"
												><img
													alt="linkedin"
													class="ml-auto min-h-[24px]"
													style="opacity: 0; transition: opacity 1200ms ease-out 0s;"
												/></a
											>
											<div class="flex mt-[16px] text-ms-gray-700">
												<div>
													<svg viewBox="0 0 12 10" class="w-[12px] h-[10px]" style="color:undefined"
														><path
															fill="currentColor"
															d="M0.519531 9.20006V6.36006C0.519531 5.26676 0.692861 4.25336 1.03953 3.32006C1.41286 2.38673 2.03953 1.46673 2.91953 0.560059L4.47953 1.72006C3.89286 2.36006 3.4662 2.96006 3.19953 3.52006C2.93286 4.05336 2.77286 4.58676 2.71953 5.12006H4.59953V9.20006H0.519531ZM7.15953 9.20006V6.36006C7.15953 5.26676 7.33283 4.25336 7.67953 3.32006C8.05283 2.38673 8.67953 1.46673 9.55953 0.560059L11.1195 1.72006C10.5328 2.36006 10.1062 2.96006 9.83953 3.52006C9.57283 4.05336 9.41283 4.58676 9.35953 5.12006H11.2395V9.20006H7.15953Z"
														/></svg
													>
												</div>
												<p
													class="!font-[400] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 ml-[8px]"
												>
													We would like to extend our heartfelt appreciation to Masai for the
													exceptional talent we have had t...
												</p>
											</div>
											<div class="flex items-center mt-[16px]" />
											<div class="flex items-center mt-[16px]">
												<img
													class="rounded-[8px] w-[48px] h-[48px] mr-[8px] min-h-[48px]"
													style="opacity: 0; transition: opacity 1200ms ease-out 0s;"
												/>
												<div>
													<p
														class="!font-[600] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 mb-[4px]"
													>
														Arshdeep Singh
													</p>
													<div class="flex">
														<p
															class="!font-[400] text-[12px] leading-[16px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 undefined"
														>
															Director of technology -
														</p>
														<p
															class="!font-[400] text-[12px] leading-[16px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 ml-[4px]"
														>
															Kapiva
														</p>
													</div>
												</div>
											</div>
											<img
												class="mt-[16px] ml-[-8px] w-[93px] min-h-[31.88px]"
												alt="company logo"
												style="height: 31.88px;"
											/></button
										>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div
						class="flex items-center pb-[10px] flex-wrap justify-between px-[16px] svelte-jnbt72"
					>
						<div slot="customPagination">
							<a
								href="https://www.masaischool.com/blog/category/impact-stories/"
								class="undefined !font-[600] text-[16px] leading-[24px] font-sans p-[12px_16px] inline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !p-0 text-[#ED0331] hover:underline"
								disabled="false"
								target="_blank">Read More</a
							>
						</div>
						<div class="flex justify-center gap-[8px] w-[fit-content]">
							<button
								type="button"
								class="!outline-offset-[5px] rounded-[0.375rem] text-[#2b6cb0] hover:bg-[#FEDFE5] border-[1px] border-[currentColor] flex justify-center items-center !font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase p-[12px_16px] inline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 company-review-card-prev text-[#ED0331] hover:text-white cursor-pointer !p-[4px] min-w-[auto] w-[32px] h-[32px] !bg-white active:!bg-[#CC032A] hover:!bg-[#ED0331] swiper-button-disabled"
								disabled=""
								><div>
									<svg
										width="24"
										height="24"
										fill="currentColor"
										viewBox="0 0 24 24"
										class=""
										xmlns="http://www.w3.org/2000/svg"
										><path
											d="M15.41 16.58L10.83 12L15.41 7.41L14 6L7.99997 12L14 18L15.41 16.58Z"
											fill="currentColor"
										/></svg
									>
								</div></button
							>
							<button
								type="button"
								class="!outline-offset-[5px] rounded-[0.375rem] text-[#2b6cb0] hover:bg-[#FEDFE5] border-[1px] border-[currentColor] flex justify-center items-center !font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase p-[12px_16px] inline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 company-review-card-next text-[#ED0331] hover:text-white cursor-pointer !p-[4px] min-w-[auto] w-[32px] h-[32px] !bg-white active:!bg-[#CC032A] hover:!bg-[#ED0331]"
								><div>
									<svg
										width="24"
										height="24"
										fill="currentColor"
										viewBox="0 0 24 24"
										class=""
										xmlns="http://www.w3.org/2000/svg"
										><path
											d="M8.59003 16.58L13.17 12L8.59003 7.41L10 6L16 12L10 18L8.59003 16.58Z"
											fill="currentColor"
										/></svg
									>
								</div></button
							>
						</div>
					</div>
				</div>
			</div> -->
		</div>
	</div>
</div>
