import sublime, sublime_plugin
from .navigate_regions import JavascriptEnhancementsNavigateRegionsCommand

class JavascriptEnhancementsNavigateFlowErrorsCommand(JavascriptEnhancementsNavigateRegionsCommand, sublime_plugin.TextCommand):
  region_key = "javascript_enhancements_flow_error"