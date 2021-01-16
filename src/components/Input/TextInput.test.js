import renderer from 'react-test-renderer';
import { TextInput } from './TextInput';

describe("<TextInput />", () => {
    it("snapshot check", () => {
        const tree = renderer.create(<TextInput placeholder="email" type="email" />).toJSON();
        expect(tree).toMatchSnapshot();
    });
});