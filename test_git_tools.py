import unittest
import git_tools as git


class GitToolsTestCase(unittest.TestCase):
    def test_local_commit_ref(self):
        self.assertEqual(git.local_commit_ref('./test_resources/test-project-1'), 'dc34719')

    def test_is_path_a_repo(self):
        self.assertTrue(git.is_path_a_repo('./test_resources/test-project-1'))
        self.assertTrue(not git.is_path_a_repo('./test_resources'))


if __name__ == '__main__':
    unittest.main()
