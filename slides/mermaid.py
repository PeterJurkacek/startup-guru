import requests

# Step 2: Send a POST request to Kroki API
kroki_url = "https://kroki.io/mermaid/svg/eNqVVc1u2zAMvusp-gAOIMl_cW9du6EDiq5oh91VR02MuVbhOOvy9pNjyxIpKe1uiShS3w9Jr1YrUqvupdlekouLveh-y-P4S__eqfdfoj3I_eXFi2j3kqz03enG6lkOgpBvTds23Ta5laIddsefSg27JKeUkhtZi2Nyo8yN06H5MwVPR_diOPSinTKd8-nnvT4dE9KspORR37kWnWjhcykvMnLdq_cOnvOqquYyd1L8kVet6mTC8nS9gLMVWc74fPz179CLemhUlzDOKLl6PgyvshumquAJxjIX1pTPGM3J99e3VnQDuk6LijyobmhqGCjXFRRirPko96p_O-Eo0oyAhAfZN2qjK-mEXooTviQvs4XZpEeeVQSVMormvIIlHY2yooQxa2NaVuRL32y2EplQIoSOimlaQnYL-mZo9to_vjTGGBFvTS3aR7FpVHuoZVcfE75mM7MfusjtcdtIDZOX5ZKIWPKCEfhKUDGec0wUus3pmkQwGSG5dttjF7jPqgq_NZnEytzpoVh2mWInrSms8Gi4ne31gNvhaQFTXYHHoGkoqAvjKO3p0G9H0FZbxjNkgVGM8XSeVzMwDMOfW0yPUkx-lwNF7fqkL58eojyWDhTS6wZpMOwm2LXDh9J4scUJivfFTNFZflCUMTKJEXOeUt95CN5rv1r1Sgfv5H7Sx6xTK8wZLnNXzldgqcXCBTWCNgZm887xhOeWTaDahDw4vgajrWY7xwsFOjRIETQWdvOMR_A1MEa-g-4HaeF4vZOvPkIzgA4xt5N8qyMY0ZNzOduePlFoEhbabXk0vebjB70953ucic1AxkRoxm12WsEZg3kwglnmkxPZBlCxQOvOn3qrsTfHdtZQ6DM0kKPRgUar25ofgAycDDekcdfSiryMZ8A3GS-y0A0rkXn484vSNRqFzu54d44j1-wuiy1bOAewbFhZv5pLwKXvj2ZoFD7e9nEc7qj7JgXd_r-PZnyjT1MTn6cz_huN_OR_udaORQ=="
response = requests.get(kroki_url, headers={"Content-Type": "text/plain"})

# Check if the request was successful
if response.status_code == 200:
    # Step 3: Save the SVG to a file
    with open("slides/img/sankey.svg", "wb") as svg_file:
        svg_file.write(response.content)
    print("SVG saved as diagram.svg")
else:
    print("problem")