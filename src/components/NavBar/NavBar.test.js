import { render } from '@testing-library/react';
import renderer from 'react-test-renderer';
import { NavBar } from './NavBar';

describe('<NavBar />', () => {
    it('snapshot check', () => {
        const tree = renderer.create(<NavBar title='My Dashboard' isLoggedIn />).toJSON();
        expect(tree).toMatchSnapshot();
    })
})