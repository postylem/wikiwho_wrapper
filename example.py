from wikiwho_wrapper import WikiWhoAPI

api = WikiWhoAPI()

# nice example: bioglass
# response = api.all_content("Cologne")
response = api.range_rev_content_by_article_title("bioglass", 18064039, 79583319)
import ipdb; ipdb.set_trace()  # breakpoint 12fb971f //

