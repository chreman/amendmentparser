# amendmentparser
This tool parses information out of an amendments proposal document and shows which parts of a report are highly controversial and who amends what.

Needs following python packages:
- networkx
- BeautifulSoup4

Use:
Rename example_config.py to config.py and edit to the correct locations of datapath and resultspath.
Datapath should contain htmls of amendment documents.

Switch to the script folder and run
python workflow.py

Expected output:
A graphml-file containing co-authors of amendments. Further processing can be done with Gephi, because it produces very nice graphics and has nice layout-algorithms.
