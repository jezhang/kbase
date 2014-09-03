package info.jezhang.controller;


@Controller
@RequestMapping("/")
public class BaseController {
	public String welcome(ModelMap model) {
		model.addAttribute("message", "Maven Web Project + Spring 3 MVC - welcome()");
		
		// spring uses InternalResourceViewResolver and return back index.jsp
		return "index"
	}
}

@RequestMapping(value="/welcome/{name}",method=RequestMethod.GET)
public String welcomeName(@PathVariable String name, ModelMap model) {
	model.addAttribute("message", "Maven Web Project + Spring 3 MVC - " + name);
	return "index";
}
