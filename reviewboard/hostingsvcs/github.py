    def api_get(self, url, *args, **kwargs):
            return data
                      'This code will be sent to you by GitHub.'))
                raise AuthorizationError(rsp['message'])
            raise HostingServiceError(rsp['message'])
            raise HostingServiceError(six.text_type(e))
class GitHub(HostingService):
    RAW_MIMETYPE = 'application/vnd.github.v3.raw'

    REFNAME_PREFIX = 'refs/heads/'
    REFNAME_PREFIX_LEN = len(REFNAME_PREFIX)

            repo_info = self._api_get_repository(
                self._get_repository_owner_raw(plan, kwargs),
                self._get_repository_name_raw(plan, kwargs))
        except Exception as e:
            if six.text_type(e) == 'Not Found':
                    # If we get a Not Found, then the authorization was
                    if six.text_type(e) != 'Not Found':
        url = self._build_api_url(self._get_repo_api_url(repository),
                                  'git/blobs/%s' % revision)

        try:
            return self.client.http_get(url, headers={
                'Accept': self.RAW_MIMETYPE,
            })[0]
        except (URLError, HTTPError):
            raise FileNotFoundError(path, revision)
        url = self._build_api_url(self._get_repo_api_url(repository),
                                  'git/blobs/%s' % revision)

            self.client.http_get(url, headers={
                'Accept': self.RAW_MIMETYPE,
            })

        except (URLError, HTTPError):

        url = self._build_api_url(self._get_repo_api_url(repository),
                                  'git/refs/heads')

        try:
            rsp = self.client.api_get(url)
        except Exception as e:
            logging.warning('Failed to fetch commits from %s: %s',
                            url, e)
            return results

        for ref in rsp:
            refname = ref['ref']

            if refname.startswith(self.REFNAME_PREFIX):
                name = refname[self.REFNAME_PREFIX_LEN:]
                results.append(Branch(id=name,
                                      commit=ref['object']['sha'],
                                      default=(name == 'master')))

        resource = 'commits'
        url = self._build_api_url(self._get_repo_api_url(repository), resource)

        if start:
            url += '&sha=%s' % start

        try:
            rsp = self.client.api_get(url)
        except Exception as e:
            logging.warning('Failed to fetch commits from %s: %s',
                            url, e)
            return results

        for item in rsp:
            url = self._build_api_url(repo_api_url, 'commits')
            url += '&sha=%s' % revision

            try:
                commit = self.client.api_get(url)[0]
            except Exception as e:
                raise SCMError(six.text_type(e))
        # Step 2: fetch the "compare two commits" API to get the diff if the
        # commit has a parent commit. Otherwise, fetch the commit itself.
        if parent_revision:
            url = self._build_api_url(
                repo_api_url, 'compare/%s...%s' % (parent_revision, revision))
        else:
            url = self._build_api_url(repo_api_url, 'commits/%s' % revision)

        try:
            comparison = self.client.api_get(url)
        except Exception as e:
            raise SCMError(six.text_type(e))

        if parent_revision:
            tree_sha = comparison['base_commit']['commit']['tree']['sha']
        else:
            tree_sha = comparison['commit']['tree']['sha']

        files = comparison['files']
        url = self._build_api_url(repo_api_url, 'git/trees/%s' % tree_sha)
        url += '&recursive=1'
        tree = self.client.api_get(url)
        example_id = 123
        example_url = build_server_url(local_site_reverse(
            'review-request-detail',
            local_site=repository.local_site,
            kwargs={
                'review_request_id': example_id,
            }))

                'example_id': example_id,
                'example_url': example_url,
        return '%s?access_token=%s' % (
            '/'.join(api_paths),
            self.account.data['authorization']['token'])
    def _api_get_repository(self, owner, repo_name):
        return self.client.api_get(self._build_api_url(
            self._get_repo_api_url_raw(owner, repo_name)))
