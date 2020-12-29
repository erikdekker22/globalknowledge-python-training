def build_url(hostname,path,resource,port=443,ext='.html'):
    returnvalue = "https://" + hostname + ':' + str(port) + '/' + path + resource + ext
    return returnvalue


def main():
    url = build_url("service.org", "api/v2/", "interfaces", port=7700, ext=".json")
    print(url)
    url = build_url("service.org", "api/v2/", "routers")
    print(url)

if __name__ == "__main__":
    main()