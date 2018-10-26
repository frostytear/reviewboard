from djblets.features.testing import override_feature_checks
from reviewboard.diffviewer.commit_utils import serialize_validation_info
        with override_feature_checks(self.override_features):
            rsp = self.api_post(
                get_draft_diffcommit_list_url(review_request,
                                              diffset.revision),
                dict(self._DEFAULT_POST_DATA, **{
                    'diff': SimpleUploadedFile('diff', b'     ',
                                               content_type='text/x-patch'),
                }),
                expected_status=400)
            with override_feature_checks(self.override_features):
                rsp = self.api_post(
                    get_draft_diffcommit_list_url(review_request,
                                                  diffset.revision),
                    dict(self._DEFAULT_POST_DATA, **{
                        'diff': diff,
                    }),
                    expected_status=400)
        with override_feature_checks(self.override_features):
            rsp = self.api_post(
                get_draft_diffcommit_list_url(review_request,
                                              diffset.revision),
                dict(self._DEFAULT_POST_DATA, **{
                    'diff': diff,
                }),
                expected_status=400)
        with override_feature_checks(self.override_features):
            rsp = self.api_post(
                get_draft_diffcommit_list_url(review_request,
                                              diffset.revision),
                dict(self._DEFAULT_POST_DATA, **{
                    'diff': diff,
                    'parent_diff': parent_diff,
                }),
                expected_mimetype=draft_diffcommit_item_mimetype)
        with override_feature_checks(self.override_features):
            rsp = self.api_post(
                get_draft_diffcommit_list_url(review_request,
                                              diffset.revision),
                dict(self._DEFAULT_POST_DATA, **{
                    'commit_id': 'r0',
                    'parent_id': 'r1',
                    'diff': diff,
                    'parent_diff': parent_diff,
                }),
                expected_mimetype=draft_diffcommit_item_mimetype,
                expected_status=201)

        with override_feature_checks(self.override_features):
            rsp = self.api_post(
                get_draft_diffcommit_list_url(review_request,
                                              diffset.revision),
                dict(self._DEFAULT_POST_DATA, **{
                    'commit_id': 'r0',
                    'parent_id': 'r1',
                    'diff': diff,
                    'committer_date': 'Jun 1 1990',
                    'author_date': 'Jun 1 1990',
                }),
                expected_status=400)
        validation_info = serialize_validation_info({
            commit.commit_id: {
                'parent_id': commit.parent_id,
                'tree': {
                    'added': [],
                    'modified': [{
                        'filename': 'readme',
                        'revision': '5b50866',
                    }],
                    'removed': [],
            },
        })
        with override_feature_checks(self.override_features):
            rsp = self.api_post(
                get_draft_diffcommit_list_url(review_request,
                                              diffset.revision),
                dict(self._DEFAULT_POST_DATA, **{
                    'commit_id': 'r2',
                    'parent_id': 'r1',
                    'diff': diff,
                    'validation_info': validation_info,
                }),
                expected_mimetype=draft_diffcommit_item_mimetype)