import renderer from 'react-test-renderer';
import { Login } from './Login';

describe("<Login />", () => {
    it("snapshot check", () => {
        const tree = renderer.create(<Login />).toJSON();
        expect(tree).toMatchSnapshot();
    });
});